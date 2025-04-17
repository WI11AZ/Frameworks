import sqlite3

from django.core.management.base import BaseCommand, CommandError

from web_app.models import Opm, DcwfWorkRole, DcwfKsat, Ncwf2017Ksat
from web_app.models.dcwf_category import DcwfCategory
from web_app.models.dcwf_work_role_ksat_relation import (
    DcwfWorkRoleKsatRelation,
    KsatRelation,
)


class Command(BaseCommand):
    help = "Imports DCWF data from the SQLite database"

    def add_arguments(self, parser):
        # Add directory of the sqlite database
        parser.add_argument("sqlite_path", type=str)

    def handle(self, *args, **options):
        db_path = options["sqlite_path"]
        with sqlite3.connect(db_path) as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            # Read and handle work roles
            cursor.execute(
                "SELECT opm_id, nist_id, title, description, url FROM workroles",
            )
            work_roles = [dict(row) for row in cursor.fetchall()]
            opm_ids = [row["opm_id"] for row in work_roles]
            self.insert_opm_ids(opm_ids)
            self.insert_work_roles(work_roles)
            # Read and handle categories
            cursor.execute(
                "SELECT title, description, url FROM workforce_elements",
            )
            categories = [dict(row) for row in cursor.fetchall()]
            self.insert_categories(categories)
            # Read work role <-> category mapping
            cursor.execute(
                "SELECT workroles.opm_id, workforce_elements.title FROM workforce_elements_workroles join workroles on workroles.id = workrole_id join workforce_elements on workforce_elements.id = workforce_element_id",
            )
            for row in cursor.fetchall():
                work_role = DcwfWorkRole.objects.get(opm_id=row["opm_id"])
                category = DcwfCategory.objects.get(title=row["title"])
                work_role.category = category
                work_role.save()
            # Read and handle ksats
            cursor.execute("SELECT * from ksats")
            ksats = [dict(row) for row in cursor.fetchall()]
            self.insert_ksats(ksats)
            # Read work role <-> ksat relations
            cursor.execute(
                "select w.opm_id, k.ksat_id, wk.type from workroles_ksats wk join workroles w on w.id  = wk.workrole_id join ksats k on k.id = wk.ksat_id;",
            )
            work_role_ksat_relations = [dict(row) for row in cursor.fetchall()]
            self.insert_work_role_ksat_relations(work_role_ksat_relations)

    def insert_opm_ids(self, opm_ids):
        # Insert OPM id if it does not yet exist
        for opm_id in opm_ids:
            if not Opm.objects.filter(id=opm_id).exists():
                Opm.objects.create(id=opm_id)
        self.stdout.write(self.style.SUCCESS("Successfully imported OPM IDs"))

    def insert_work_roles(self, work_roles):
        # Remove all existing work roles
        DcwfWorkRole.objects.all().delete()
        # Insert work roles
        for work_role in work_roles:
            DcwfWorkRole.objects.create(
                opm_id=work_role["opm_id"],
                nist_id=work_role["nist_id"],
                title=work_role["title"],
                description=work_role["description"],
                url=work_role["url"],
            )
        self.stdout.write(self.style.SUCCESS("Successfully imported work roles"))

    def insert_categories(self, categories):
        # Remove all existing categories
        DcwfCategory.objects.all().delete()
        # Insert categories
        for category in categories:
            DcwfCategory.objects.create(
                title=category["title"],
                description=category["description"],
                url=category["url"],
            )
        self.stdout.write(self.style.SUCCESS("Successfully imported categories"))

    def insert_ksats(self, ksats):
        # Remove all existing ksats
        DcwfKsat.objects.all().delete()
        # Insert ksats
        for ksat in ksats:
            try:
                ncwf_ksat = (
                    Ncwf2017Ksat.objects.get(ncwf_id=ksat["nist_id"])
                    if ksat["nist_id"]
                    else None
                )
            except Ncwf2017Ksat.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f"KSAT {ksat['nist_id']} not found in NCWF 2017")
                )
            DcwfKsat.objects.create(
                dcwf_id=ksat["ksat_id"],
                url=ksat["url"],
                description=ksat["description"],
                category=ksat["category"].lower(),
                ncwf_2017_ksat=ncwf_ksat,
            )
        self.stdout.write(self.style.SUCCESS("Successfully imported ksats"))

    def insert_work_role_ksat_relations(self, work_role_ksat_relations):
        # Insert work role <-> ksat relations
        for relation in work_role_ksat_relations:
            work_role = DcwfWorkRole.objects.get(opm_id=relation["opm_id"])
            ksat = DcwfKsat.objects.get(dcwf_id=relation["ksat_id"])
            type = (
                KsatRelation.CORE
                if relation["type"].lower() == "core"
                else KsatRelation.ADDITIONAL
            )
            try:
                DcwfWorkRoleKsatRelation.objects.create(
                    dcwf_work_role=work_role,
                    dcwf_ksat=ksat,
                    type=type,
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(
                        f"Could not create relation between {relation["opm_id"]} and {relation["ksat_id"]}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully imported work role <-> ksat relations")
        )
