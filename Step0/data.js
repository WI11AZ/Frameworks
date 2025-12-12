// Données complètes NCWF & DCWF 2025
const allRolesData = [
    // ========== IMPLEMENTATION & OPERATION (IO) ==========
    {
        ncwf_id: "IO-WRL-002",
        opm_code: 421,
        dcwf: {
            work_role: "Database Administrator",
            code: 421,
            element: "Information Technology (IT)",
            definition: "Administers databases and/or data management systems that allow for the storage, query, and utilization of data."
        },
        nice: {
            work_role: "Database Administration",
            id: "IO-WRL-002",
            description: "Responsible for administering databases and data management systems that allow for the secure storage, query, protection, and utilization of data.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" },
                { name: "Data Analysis", percentage: "50%" }
            ],
            on_ramps: ["Data Analysis", "Knowledge Management", "Network Operations", "Systems Administration", "Technical Support"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Data Analysis", "Network Operations", "Privacy Compliance", "Product Support Management", "Secure Project Management", "Secure Software Development", "Systems Administration", "Systems Requirements Planning"],
            top_5_secondary: [
                { name: "Data Analysis", percentage: "23.49%" },
                { name: "Systems Administration", percentage: "22.65%" },
                { name: "Technical Support", percentage: "15.32%" },
                { name: "Knowledge Management", percentage: "5.73%" },
                { name: "Secure Software Development", percentage: "5.21%" }
            ]
        }
    },
    {
        ncwf_id: "IO-WRL-003",
        opm_code: 431,
        dcwf: {
            work_role: "Knowledge Manager",
            code: 431,
            element: "Information Technology (IT)",
            definition: "Responsible for the management and administration of processes and tools that enable the organization to identify, document, and access intellectual capital and information content."
        },
        nice: {
            work_role: "Knowledge Management",
            id: "IO-WRL-003",
            description: "Responsible for managing and administering processes and tools to identify, document, and access an organization's intellectual capital.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Communications Security (COMSEC) Management", percentage: "65.52%" },
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Technology Research and Development", percentage: "62.96%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Data Analysis", percentage: "50%" }
            ],
            on_ramps: ["Data Analysis", "Systems Requirements Planning", "Technical Support"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Data Analysis", "Database Administration", "Privacy Compliance", "Product Support Management", "Secure Project Management"],
            top_5_secondary: [
                { name: "Technical Support", percentage: "21.69%" },
                { name: "Program Management", percentage: "13.59%" },
                { name: "Systems Administration", percentage: "7.99%" },
                { name: "Data Analysis", percentage: "7.15%" },
                { name: "Database Administration", percentage: "5.13%" }
            ]
        }
    },
    {
        ncwf_id: "IO-WRL-004",
        opm_code: 441,
        dcwf: {
            work_role: "Network Operations Specialist",
            code: 441,
            element: "Information Technology (IT)",
            definition: "Plans, implements, and operates network services/systems, to include hardware and virtual environments."
        },
        nice: {
            work_role: "Network Operations",
            id: "IO-WRL-004",
            description: "Responsible for planning, implementing, and operating network services and systems, including hardware and virtual environments.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "68%" },
                { name: "Technology Research and Development", percentage: "62.96%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Enterprise Architecture", percentage: "59.26%" },
                { name: "Systems Authorization", percentage: "58.7%" }
            ],
            on_ramps: ["Database Administration", "Systems Administration", "Technical Support"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Database Administration", "Defensive Cybersecurity", "Infrastructure Support", "Privacy Compliance", "Product Support Management", "Secure Project Management", "Secure Systems Development", "Systems Requirements Planning", "Systems Security Analysis", "Systems Security Management", "Systems Testing and Evaluation", "Vulnerability Analysis"],
            top_5_secondary: [
                { name: "Technical Support", percentage: "32.97%" },
                { name: "Systems Administration", percentage: "25.67%" },
                { name: "Infrastructure Support", percentage: "6.49%" },
                { name: "Systems Requirements Planning", percentage: "4.6%" },
                { name: "Program Management", percentage: "3.85%" }
            ]
        }
    },
    {
        ncwf_id: "IO-WRL-005",
        opm_code: 451,
        dcwf: {
            work_role: "System Administrator",
            code: 451,
            element: "Information Technology (IT)",
            definition: "Installs, configures, troubleshoots, and maintains hardware, software, and administers system accounts."
        },
        nice: {
            work_role: "Systems Administration",
            id: "IO-WRL-005",
            description: "Responsible for setting up and maintaining a system or specific components of a system in adherence with organizational security policies and procedures. Includes hardware and software installation, configuration, and updates; user account management; backup and recovery management; and security control implementation.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Cybersecurity Legal Advice", percentage: "81.48%" },
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" },
                { name: "Data Analysis", percentage: "50%" }
            ],
            on_ramps: ["Database Administration", "Technical Support"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Database Administration", "Defensive Cybersecurity", "Infrastructure Support", "Network Operations", "Privacy Compliance", "Product Support Management", "Secure Project Management", "Secure Software Development", "Systems Requirements Planning", "Systems Security Analysis", "Systems Testing and Evaluation", "Vulnerability Analysis"],
            top_5_secondary: [
                { name: "Technical Support", percentage: "41.3%" },
                { name: "Database Administration", percentage: "10.26%" },
                { name: "Network Operations", percentage: "9.48%" },
                { name: "Systems Security Analysis", percentage: "8.39%" },
                { name: "Systems Requirements Planning", percentage: "3.81%" }
            ]
        }
    },
    {
        ncwf_id: "IO-WRL-006",
        opm_code: 461,
        dcwf: {
            work_role: "Systems Security Analyst",
            code: 461,
            element: "Software Engineering (SE)",
            definition: "Responsible for analysis and development of systems/software security through the product lifecycle to include integration, testing, operations and maintenance."
        },
        nice: {
            work_role: "Systems Security Analysis",
            id: "IO-WRL-006",
            description: "Responsible for developing and analyzing the integration, testing, operations, and maintenance of systems security. Prepares, performs, and manages the security aspects of implementing and operating a system.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "72%" },
                { name: "Systems Authorization", percentage: "71.74%" },
                { name: "Communications Security (COMSEC) Management", percentage: "68.97%" },
                { name: "Cybersecurity Legal Advice", percentage: "66.67%" },
                { name: "Technology Research and Development", percentage: "62.96%" }
            ],
            on_ramps: ["Data Analysis", "Network Operations", "Secure Software Development", "Security Control Assessment", "Systems Administration", "Systems Testing and Evaluation"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Defensive Cybersecurity", "Incident Response", "Infrastructure Support", "Product Support Management", "Secure Project Management", "Security Control Assessment", "Systems Security Management", "Vulnerability Analysis"],
            top_5_secondary: [
                { name: "Technical Support", percentage: "13.56%" },
                { name: "Vulnerability Analysis", percentage: "12.1%" },
                { name: "Security Control Assessment", percentage: "10.32%" },
                { name: "Systems Security Management", percentage: "8.13%" },
                { name: "Systems Administration", percentage: "7.61%" }
            ]
        }
    },
    {
        ncwf_id: "IO-WRL-007",
        opm_code: 411,
        dcwf: {
            work_role: "Technical Support Specialist",
            code: 411,
            element: "Information Technology (IT)",
            definition: "Provides technical support to customers who need assistance utilizing client level hardware and software in accordance with established or approved organizational process components. (i.e., Master Incident Management Plan, when applicable)."
        },
        nice: {
            work_role: "Technical Support",
            id: "IO-WRL-007",
            description: "Responsible for providing technical support to customers who need assistance utilizing client-level hardware and software in accordance with established or approved organizational policies and processes.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Cybersecurity Legal Advice", percentage: "81.48%" },
                { name: "Communications Security (COMSEC) Management", percentage: "65.52%" },
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Data Analysis", percentage: "50%" }
            ],
            on_ramps: [],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Data Analysis", "Database Administration", "Knowledge Management", "Network Operations", "Privacy Compliance", "Product Support Management", "Secure Project Management", "Systems Administration", "Systems Testing and Evaluation"],
            top_5_secondary: [
                { name: "Systems Administration", percentage: "43.69%" },
                { name: "Network Operations", percentage: "17.16%" },
                { name: "Knowledge Management", percentage: "5.85%" },
                { name: "Data Analysis", percentage: "4.29%" },
                { name: "Database Administration", percentage: "4.23%" }
            ]
        }
    },
    {
        ncwf_id: "IO-WRL-001",
        opm_code: 422,
        dcwf: {
            work_role: "Data Analyst",
            code: 422,
            element: "Data/AI (DA)",
            definition: "Analyzes and interprets data from multiple disparate sources and builds visualizations and dashboards to report insights."
        },
        nice: {
            work_role: "Data Analysis",
            id: "IO-WRL-001",
            description: "Responsible for analyzing data from multiple disparate sources to provide cybersecurity and privacy insight. Designs and implements custom algorithms, workflow processes, and layouts for complex, enterprise-scale data sets used for modeling, data mining, and research purposes.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" },
                { name: "Database Administration", percentage: "45.71%" }
            ],
            on_ramps: ["Database Administration", "Knowledge Management", "Secure Software Development", "Secure Systems Development", "Technical Support"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Database Administration", "Defensive Cybersecurity", "Knowledge Management", "Privacy Compliance", "Product Support Management", "Secure Project Management", "Secure Software Development", "Secure Systems Development", "Systems Security Analysis", "Technology Research and Development"],
            top_5_secondary: [
                { name: "Knowledge Management", percentage: "22.42%" },
                { name: "Database Administration", percentage: "14.32%" },
                { name: "Secure Software Development", percentage: "9.59%" },
                { name: "Systems Requirements Planning", percentage: "7.85%" },
                { name: "Technical Support", percentage: "7.1%" }
            ]
        }
    },

    // ========== OVERSIGHT & GOVERNANCE (OG) ==========
    {
        ncwf_id: "OG-WRL-001",
        opm_code: 723,
        dcwf: {
            work_role: "COMSEC Manager",
            code: 723,
            element: "Cybersecurity (CS)",
            definition: "Manages the Communications Security (COMSEC) resources of an organization (CNSSI No. 4009)."
        },
        nice: {
            work_role: "Communications Security (COMSEC) Management",
            id: "OG-WRL-001",
            description: "Responsible for managing the Communications Security (COMSEC) resources of an organization.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "68%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Data Analysis", percentage: "50%" },
                { name: "Database Administration", percentage: "45.71%" }
            ],
            on_ramps: ["Systems Security Management"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Secure Project Management", "Systems Security Management"],
            top_5_secondary: [
                { name: "Systems Security Management", percentage: "12.9%" },
                { name: "Systems Administration", percentage: "12.1%" },
                { name: "Technical Support", percentage: "12.1%" },
                { name: "Communications Security (COMSEC) Management", percentage: "5.65%" },
                { name: "Secure Project Management", percentage: "5.24%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-002",
        opm_code: 752,
        dcwf: {
            work_role: "Cyber Policy and Strategy Planner",
            code: 752,
            element: "Cyber Enablers (EN)",
            definition: "Develops cyberspace plans, strategy and policy to support and align with organizational cyberspace missions and initiatives."
        },
        nice: {
            work_role: "Cybersecurity Policy and Planning",
            id: "OG-WRL-002",
            description: "Responsible for developing and maintaining cybersecurity plans, strategy, and policy to support and align with organizational cybersecurity initiatives and regulatory compliance.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "68%" },
                { name: "Technology Program Auditing", percentage: "64.86%" },
                { name: "Technology Research and Development", percentage: "62.96%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" }
            ],
            on_ramps: ["Cybercrime Investigation", "Cybersecurity Architecture", "Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Legal Advice", "Cybersecurity Workforce Management", "Data Analysis", "Database Administration", "Defensive Cybersecurity", "Digital Evidence Analysis", "Digital Forensics", "Enterprise Architecture", "Incident Response", "Infrastructure Support", "Knowledge Management", "Network Operations", "Privacy Compliance", "Product Support Management", "Program Management", "Secure Project Management", "Secure Software Development", "Secure Systems Development", "Security Control Assessment", "Software Security Assessment", "Systems Administration", "Systems Authorization", "Systems Requirements Planning", "Systems Security Analysis", "Systems Security Management", "Systems Testing and Evaluation", "Technical Support", "Technology Portfolio Management", "Technology Program Auditing", "Technology Research and Development", "Vulnerability Analysis"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Workforce Management", "Executive Cybersecurity Leadership", "Privacy Compliance", "Program Management", "Secure Project Management", "Systems Authorization"],
            top_5_secondary: [
                { name: "Program Management", percentage: "17.1%" },
                { name: "Secure Project Management", percentage: "9.28%" },
                { name: "Cybersecurity Workforce Management", percentage: "8.24%" },
                { name: "Systems Requirements Planning", percentage: "8.03%" },
                { name: "Systems Security Management", percentage: "6.47%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-003",
        opm_code: 751,
        dcwf: {
            work_role: "Cyber Workforce Developer and Manager",
            code: 751,
            element: "Cyber Enablers (EN)",
            definition: "Develop cyberspace workforce plans, strategies and guidance to support cyberspace workforce manpower, personnel, training and education requirements and to address changes to cyberspace policy, doctrine, materiel, force structure, and education and training requirements."
        },
        nice: {
            work_role: "Cybersecurity Workforce Management",
            id: "OG-WRL-003",
            description: "Responsible for developing cybersecurity workforce plans, assessments, strategies, and guidance, including cybersecurity-related staff training, education, and hiring processes. Makes adjustments in response to or in anticipation of changes to cybersecurity-related policy, technology, and staffing needs and requirements. Authors mandated workforce planning strategies to maintain compliance with legislation, regulation, and policy.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "68%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" },
                { name: "Data Analysis", percentage: "50%" }
            ],
            on_ramps: ["Cybercrime Investigation", "Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Data Analysis", "Database Administration", "Defensive Cybersecurity", "Digital Evidence Analysis", "Digital Forensics", "Incident Response", "Infrastructure Support", "Knowledge Management", "Network Operations", "Privacy Compliance", "Product Support Management", "Program Management", "Secure Project Management", "Secure Software Development", "Secure Systems Development", "Security Control Assessment", "Software Security Assessment", "Systems Administration", "Systems Requirements Planning", "Systems Security Analysis", "Systems Security Management", "Systems Testing and Evaluation", "Technical Support", "Technology Research and Development", "Vulnerability Analysis"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Secure Project Management"],
            top_5_secondary: [
                { name: "Cybersecurity Policy and Planning", percentage: "34.51%" },
                { name: "Program Management", percentage: "21.77%" },
                { name: "Secure Project Management", percentage: "5.84%" },
                { name: "Systems Security Management", percentage: "5.84%" },
                { name: "Systems Requirements Planning", percentage: "3.89%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-004",
        opm_code: 711,
        dcwf: {
            work_role: "Cyber Instructional Curriculum Developer",
            code: 711,
            element: "Cyber Enablers (EN)",
            definition: "Develops, plans, coordinates, and evaluates cyber training/education courses, methods, and techniques based on instructional needs."
        },
        nice: {
            work_role: "Cybersecurity Curriculum Development",
            id: "OG-WRL-004",
            description: "Responsible for developing, planning, coordinating, and evaluating cybersecurity awareness, training, or education content, methods, and techniques based on instructional needs and requirements.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" },
                { name: "Data Analysis", percentage: "50%" }
            ],
            on_ramps: ["Communications Security (COMSEC) Management", "Cybercrime Investigation", "Cybersecurity Architecture", "Cybersecurity Instruction", "Cybersecurity Legal Advice", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Data Analysis", "Database Administration", "Defensive Cybersecurity", "Digital Evidence Analysis", "Digital Forensics", "Enterprise Architecture", "Incident Response", "Infrastructure Support", "Knowledge Management", "Network Operations", "Privacy Compliance", "Secure Project Management", "Secure Software Development", "Secure Systems Development", "Security Control Assessment", "Software Security Assessment", "Systems Administration", "Systems Requirements Planning", "Systems Security Analysis", "Systems Security Management", "Systems Testing and Evaluation", "Technical Support", "Technology Research and Development", "Vulnerability Analysis"],
            off_ramps: ["Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Secure Project Management"],
            top_5_secondary: [
                { name: "Cybersecurity Instruction", percentage: "40.26%" },
                { name: "Technical Support", percentage: "17.53%" },
                { name: "Cybersecurity Workforce Management", percentage: "11.69%" },
                { name: "Program Management", percentage: "7.79%" },
                { name: "Vulnerability Analysis", percentage: "3.25%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-005",
        opm_code: 712,
        dcwf: {
            work_role: "Cyber Instructor",
            code: 712,
            element: "Cyber Enablers (EN)",
            definition: "Develops and conducts training or education of personnel within cyber domain."
        },
        nice: {
            work_role: "Cybersecurity Instruction",
            id: "OG-WRL-005",
            description: "Responsible for developing and conducting cybersecurity awareness, training, or education.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Technology Research and Development", percentage: "66.67%" },
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Cybersecurity Legal Advice", percentage: "59.26%" },
                { name: "Cybersecurity Curriculum Development", percentage: "58.33%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" }
            ],
            on_ramps: ["Communications Security (COMSEC) Management", "Cybercrime Investigation", "Cybersecurity Architecture", "Cybersecurity Curriculum Development", "Cybersecurity Legal Advice", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Data Analysis", "Database Administration", "Defensive Cybersecurity", "Digital Evidence Analysis", "Digital Forensics", "Enterprise Architecture", "Incident Response", "Infrastructure Support", "Knowledge Management", "Network Operations", "Privacy Compliance", "Secure Software Development", "Secure Systems Development", "Security Control Assessment", "Software Security Assessment", "Systems Administration", "Systems Requirements Planning", "Systems Security Analysis", "Systems Security Management", "Systems Testing and Evaluation", "Technical Support", "Technology Research and Development", "Vulnerability Analysis"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Secure Project Management"],
            top_5_secondary: [
                { name: "Cybersecurity Curriculum Development", percentage: "57.14%" },
                { name: "Cybersecurity Policy and Planning", percentage: "16.07%" },
                { name: "Systems Security Management", percentage: "10.71%" },
                { name: "Program Management", percentage: "3.57%" },
                { name: "Systems Testing and Evaluation", percentage: "1.79%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-006",
        opm_code: 731,
        dcwf: {
            work_role: "Cyber Legal Advisor",
            code: 731,
            element: "Cyber Enablers (EN)",
            definition: "Provides legal advice and recommendations on relevant topics related to cyber law."
        },
        nice: {
            work_role: "Cybersecurity Legal Advice",
            id: "OG-WRL-006",
            description: "Responsible for providing cybersecurity legal advice and recommendations, including monitoring related legislation and regulations.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "55.17%" },
                { name: "Data Analysis", percentage: "50%" },
                { name: "Database Administration", percentage: "45.71%" }
            ],
            on_ramps: [],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Executive Cybersecurity Leadership", "Privacy Compliance"],
            top_5_secondary: [
                { name: "Data Analysis", percentage: "34.29%" },
                { name: "Privacy Compliance", percentage: "20%" },
                { name: "Cybersecurity Policy and Planning", percentage: "15.71%" },
                { name: "Technical Support", percentage: "7.14%" },
                { name: "Cybercrime Investigation", percentage: "5.71%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-007",
        opm_code: 901,
        dcwf: {
            work_role: "Executive Cyber Leader",
            code: 901,
            element: "Cyber Enablers (EN)",
            definition: "Executes decision-making authorities and establishes vision and direction for an organization's cyber and cyber-related policies, resources, and/or operations, while maintaining responsibility for risk-related decisions affecting mission success."
        },
        nice: {
            work_role: "Executive Cybersecurity Leadership",
            id: "OG-WRL-007",
            description: "Responsible for establishing vision and direction for an organization's cybersecurity operations and resources and their impact on digital and physical spaces. Possesses authority to make and execute decisions that impact an organization broadly, including policy approval and stakeholder engagement.",
            element: "Oversight & Governance",
            related_roles_tks: [
                { name: "Cybersecurity Legal Advice", percentage: "52.54%" },
                { name: "Cybersecurity Policy and Planning", percentage: "44.12%" },
                { name: "Technology Portfolio Management", percentage: "41.67%" },
                { name: "Systems Authorization", percentage: "37.86%" },
                { name: "Cybersecurity Curriculum Development", percentage: "32.67%" }
            ],
            on_ramps: ["Cybersecurity Architecture", "Cybersecurity Legal Advice", "Cybersecurity Policy and Planning", "Enterprise Architecture", "Program Management", "Systems Authorization", "Systems Security Management", "Technology Portfolio Management", "Technology Program Auditing"],
            off_ramps: ["Systems Authorization"],
            top_5_secondary: [
                { name: "Program Management", percentage: "21.15%" },
                { name: "Cybersecurity Policy and Planning", percentage: "12.25%" },
                { name: "Systems Authorization", percentage: "10.08%" },
                { name: "Cybersecurity Workforce Management", percentage: "8.3%" },
                { name: "Secure Project Management", percentage: "7.31%" }
            ]
        }
    },
    {
        ncwf_id: "OG-WRL-008",
        opm_code: 732,
        dcwf: {
            work_role: "Privacy Compliance Manager",
            code: 732,
            element: "Cyber Enablers (EN)",
            definition: "Develops and oversees privacy compliance program and privacy program staff, supporting privacy compliance needs of privacy and security executives and their teams."
        },
        nice: {
            work_role: "Privacy Compliance",
            id: "OG-WRL-008",
            description: "Responsible for developing and overseeing an organization's privacy compliance program and staff, including establishing and managing privacy-related governance, policy, and incident response needs.",
            element: "Implementation & Operation",
            related_roles_tks: [
                { name: "Technology Portfolio Management", percentage: "64%" },
                { name: "Cybersecurity Legal Advice", percentage: "62.96%" },
                { name: "Cybersecurity Curriculum Development", percentage: "61.11%" },
                { name: "Technology Research and Development", percentage: "59.26%" },
                { name: "Communications Security (COMSEC) Management", percentage: "58.62%" }
            ],
            on_ramps: ["Cybersecurity Legal Advice", "Cybersecurity Policy and Planning", "Data Analysis", "Database Administration", "Incident Response", "Knowledge Management", "Network Operations", "Product Support Management", "Secure Project Management", "Secure Software Development", "Secure Systems Development", "Security Control Assessment", "Systems Administration", "Systems Requirements Planning", "Systems Security Management", "Systems Testing and Evaluation", "Technical Support", "Technology Program Auditing", "Technology Research and Development"],
            off_ramps: ["Cybersecurity Curriculum Development", "Cybersecurity Instruction", "Cybersecurity Policy and Planning", "Cybersecurity Workforce Management", "Secure Project Management", "Systems Security Management"],
            top_5_secondary: [
                { name: "Cybersecurity Policy and Planning", percentage: "16.82%" },
                { name: "Cybersecurity Legal Advice", percentage: "15.89%" },
                { name: "Knowledge Management", percentage: "11.21%" },
                { name: "Program Management", percentage: "7.48%" },
                { name: "Cybersecurity Workforce Management", percentage: "4.67%" }
            ]
        }
    }
];

