import sqlite3

def init_db():
    connect = sqlite3.connect('SMS.db')
    cursor = connect.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT,
            student_number TEXT UNIQUE NOT NULL,
            college TEXT,
            major TEXT,
            class TEXT,
            grade TEXT,
            campus TEXT,
            ethnicity TEXT,
            direction TEXT,
            political_status TEXT,
            email TEXT,
            phone TEXT,
            wechat TEXT,
            qq TEXT,
            password TEXT
        )
    ''')
    cursor.execute('PRAGMA table_info(students)')
    columns = [column[1] for column in cursor.fetchall()]
    if 'password' not in columns:
        cursor.execute('ALTER TABLE students ADD COLUMN password TEXT')

    # 云顶简介
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS introduction (
            introduction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT DEFAULT '云顶书院简介',
            content TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
            INSERT INTO introduction (title, content)
            SELECT '云顶书院简介', '云顶书院通过构建融通网络世界与现实世界的泛在学习社区，面向全校不分专业招募选拔本科新生，建立基于梦想驱动的学习共同体，针对学生成长不同阶段提供循序渐进的梯度培育，引导成员突破影响成长的思维桎梏，激励学生在广泛的学科渗透和文化浸润中协调发展，进而实现自主性、包容性、开放性的新型学生教育管理制度。'
            WHERE NOT EXISTS (SELECT 1 FROM introduction)
        ''')

    # 公告栏
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS announcements (
            announcement_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            publish_date DATE DEFAULT CURRENT_DATE,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    cursor.execute('''
            INSERT INTO announcements (title, content, publish_date)
            SELECT '欢迎大家来到云顶书院', '云顶书院2025年春季学期正式启动，请所有新生及时完成注册。', '2025-03-01'
            WHERE NOT EXISTS (SELECT 1 FROM announcements)
        ''')

    connect.commit()
    connect.close()