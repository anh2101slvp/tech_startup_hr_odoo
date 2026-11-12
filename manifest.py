{
    'name': 'Tech Startup HR Management',
    'version': '20.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Quản lý nhân sự, ma trận kỹ năng và phân bổ dự án cho Tech Startup',
    'description': """
        Đồ án quản lý nhân sự chuyên dụng cho công ty công nghệ:
        - Quản lý Skill Matrix (Thành viên 1)
        - Ghép nối nhân sự dự án (Thành viên 2)
        - Quản lý WFH & OT (Thành viên 3)
        - Đánh giá KPI & Dashboard (Thành viên 4)
    """,
    'author': 'Nhóm Đại học - Tech Startup Project',
    'depends': ['base', 'hr', 'project', 'hr_attendance'],
    'data': [
        # 1. Phần phân quyền bảo mật (Thành viên 4)
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        
        # 2. Phần dữ liệu mồi / Demo data (Thành viên 1)
        'data/tech_skill_data.xml',
        'data/employee_demo_data.xml',
        
        # 3. Phần giao diện XML của các phân hệ (Thành viên 1, 2, 3, 4)
        'views/hr_employee_views.xml',
        'views/project_allocation_views.xml',
        'views/hr_overtime_views.xml',
        'views/tech_kpi_views.xml',
        'views/hr_dashboard_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}