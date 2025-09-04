
import sqlite3

from django.core.management.base import BaseCommand

from web_app.models import Opm, Ncwf2017Ksat, Ncwf2024Tks
from web_app.models.ncwf_2017_work_role import Ncwf2017WorkRole
from web_app.models.ncwf_2024_work_role import Ncwf2024WorkRole


class Command(BaseCommand):
    help = "Imports NCWF data from the SQLite database"

    def add_arguments(self, parser):
        # Add directory of the sqlite database
        parser.add_argument("sqlite_path", type=str)

    def handle(self, *args, **options):
        db_path = options["sqlite_path"]
        with sqlite3.connect(db_path) as db:
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            # Read opm ids
            cursor.execute(
                "SELECT opm_id FROM work_roles_opms",
            )
            opm_ids = [row["opm_id"] for row in cursor.fetchall()]
            self.insert_opm_ids(opm_ids)
            # Read and handle work roles
            cursor.execute(
                "SELECT * FROM work_roles",
            )
            work_roles = [dict(row) for row in cursor.fetchall()]
            self.insert_work_roles(work_roles)
            # Read work role opm relations - Debug the table structure first
            cursor.execute("PRAGMA table_info(work_roles_opms);")
            table_info = cursor.fetchall()
            print(f"DEBUG: work_roles_opms table structure: {table_info}")
            
            cursor.execute("SELECT * FROM work_roles_opms LIMIT 5;")
            sample_data = cursor.fetchall()
            print(f"DEBUG: Sample work_roles_opms data: {sample_data}")
            
            # Read work role opm relations
            cursor.execute(
                "SELECT wr.nist_id_2017, wo.opm_id FROM work_roles_opms wo join work_roles wr on wo.work_role_id = wr.id;",
            )
            work_role_opm_relations = [dict(row) for row in cursor.fetchall()]
            print(f"DEBUG: Found {len(work_role_opm_relations)} NCWF 2017 OPM relations")
            self.insert_work_role_opm_relations_for_ncwf_2017(work_role_opm_relations)
            cursor.execute(
                "SELECT wr.nist_id_2024, wo.opm_id FROM work_roles_opms wo join work_roles wr on wo.work_role_id = wr.id;",
            )
            work_role_opm_relations = [dict(row) for row in cursor.fetchall()]
            print(f"DEBUG: Found {len(work_role_opm_relations)} NCWF 2024 OPM relations")
            self.insert_work_role_opm_relations_for_ncwf_2024(work_role_opm_relations)
            # Read ksat data
            cursor.execute(
                "SELECT * FROM ksats",
            )
            ksats = [dict(row) for row in cursor.fetchall()]
            self.insert_ksats(ksats)
            # Read tks data
            cursor.execute(
                "SELECT * FROM tks",
            )
            tksen = [dict(row) for row in cursor.fetchall()]
            self.insert_tks(tksen)
            # Read ksat-tks relations
            cursor.execute(
                "select t.nist_id_2024, k.nist_id_2017 from tks_ksat tk inner join ksats k on tk.ksat_id = k.id join tks t on tk.tks_id = t.id;"
            )
            ksat_tks_relations = [dict(row) for row in cursor.fetchall()]
            self.insert_ksat_tks_relations(ksat_tks_relations)
            # Read work_role-ksat relations
            cursor.execute(
                "select k.nist_id_2017 as ksat_id_2017, wr.nist_id_2017 as work_role_id_2017 from work_roles_ksats wrk join ksats k on k.id = wrk.ksat_id join work_roles wr on wrk.id;"
            )
            work_role_ksat_relations = [dict(row) for row in cursor.fetchall()]
            self.insert_work_role_ksat_relations(work_role_ksat_relations)
            # Read work_role-tks relations
            cursor.execute(
                "select t.nist_id_2024 as tks_id_2024, wr.nist_id_2024 as work_role_id_2024 from work_roles_tks wrt join tks t on t.id = wrt.tks_id join work_roles wr on wrt.id where wr.nist_id_2024 is not null;"
            )
            work_role_tks_relations = [dict(row) for row in cursor.fetchall()]
            self.insert_work_role_tks_relations(work_role_tks_relations)

    def insert_opm_ids(self, opm_ids):
        # Insert OPM id if it does not yet exist
        for opm_id in opm_ids:
            if not Opm.objects.filter(id=opm_id).exists():
                Opm.objects.create(id=opm_id)
        pass

    def insert_work_roles(self, work_roles):
        # Remove all existing work roles
        Ncwf2017WorkRole.objects.all().delete()
        Ncwf2024WorkRole.objects.all().delete()
        # Insert work roles
        for work_role in work_roles:
            ncwf_2017_work_role = Ncwf2017WorkRole.objects.create(
                nist_id=work_role["nist_id_2017"],
                title=work_role["title_2017"],
                description=work_role["description_2017"],
            )
            ncwf_2024_work_role = Ncwf2024WorkRole.objects.create(
                nist_id=work_role["nist_id_2024"],
                title=work_role["title_2024"],
                description=work_role["description_2024"],
            )
            ncwf_2017_work_role.ncwf_2024_workroles.add(ncwf_2024_work_role)
            ncwf_2017_work_role.save()
        pass

    def insert_ksats(self, ksats):
        # Remove all existing ksats
        Ncwf2017Ksat.objects.all().delete()
        # Insert ksats
        for ksat in ksats:
            Ncwf2017Ksat.objects.create(
                ncwf_id=ksat["nist_id_2017"],
                description=ksat["description_2017"],
                category=ksat["category_2017"],
            )
        pass

    def insert_tks(self, tksen):
        # Remove all existing ksats
        Ncwf2024Tks.objects.all().delete()
        # Insert tksen
        for tks in tksen:
            Ncwf2024Tks.objects.create(
                ncwf_id=tks["nist_id_2024"],
                description=tks["description_2024"],
                category=tks["category_2024"],
            )
        pass

    def insert_ksat_tks_relations(self, ksat_tks_relations):
        # Insert ksat-tks relations
        for relation in ksat_tks_relations:
            try:
                ksat = Ncwf2017Ksat.objects.get(ncwf_id=relation["nist_id_2017"])
            except Exception as e:
                return
            try:
                tks = Ncwf2024Tks.objects.get(ncwf_id=relation["nist_id_2024"])
            except Ncwf2024Tks.DoesNotExist:
                return
            ksat.ncwf_2024_tks.add(tks)
            ksat.save()
        pass

    def insert_work_role_ksat_relations(self, work_role_ksat_relations):
        # Insert work_role-ksat relations
        for relation in work_role_ksat_relations:
            work_role = Ncwf2017WorkRole.objects.get(
                nist_id=relation["work_role_id_2017"]
            )
            ksat = Ncwf2017Ksat.objects.get(ncwf_id=relation["ksat_id_2017"])
            work_role.ncwf_2017_ksats.add(ksat)
            work_role.save()
        pass

    def insert_work_role_tks_relations(self, work_role_tks_relations):
        # Insert work_role-tks relations
        for relation in work_role_tks_relations:
            work_role = Ncwf2024WorkRole.objects.get(
                nist_id=relation["work_role_id_2024"]
            )
            tks = Ncwf2024Tks.objects.get(ncwf_id=relation["tks_id_2024"])
            work_role.ncwf_2024_tks.add(tks)
            work_role.save()
        pass

    def insert_work_role_opm_relations_for_ncwf_2024(self, work_role_opm_relations):
        # Insert work_role-opm relations
        for relation in work_role_opm_relations:
            work_role = Ncwf2024WorkRole.objects.get(nist_id=relation["nist_id_2024"])
            opm = Opm.objects.get(id=relation["opm_id"])
            work_role.opms.add(opm)
            work_role.save()
        pass

    def insert_work_role_opm_relations_for_ncwf_2017(self, work_role_opm_relations):
        # Insert work_role-opm relations
        for relation in work_role_opm_relations:
            work_role = Ncwf2017WorkRole.objects.get(nist_id=relation["nist_id_2017"])
            opm = Opm.objects.get(id=relation["opm_id"])
            work_role.opms.add(opm)
            work_role.save()
        pass
