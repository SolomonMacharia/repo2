
def database_tables():
    '''creates database table schema'''
    users_table = '''CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(30) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        is_admin BOOLEAN,
        registered_on VARCHAR(50)
    );'''
    print('Creating users table....')

    meetups_table = '''CREATE TABLE IF NOT EXISTS meetups(
        id SERIAL PRIMARY KEY,
        images VARCHAR(255) NOT NULL,
        topic VARCHAR(255) NOT NULL,
        happening_on VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        tags VARCHAR(255),
        created_by INTEGER REFERENCES users (id),
        created_on VARCHAR(50)
    );'''
    print('Creating meetups_table....')

    questions_table = '''CREATE TABLE IF NOT EXISTS questions(
        id SERIAL PRIMARY KEY,
        created_by INTEGER NOT NULL REFERENCES users (id),
        meetup_id INTEGER NOT NULL REFERENCES meetups (id),
        created_on VARCHAR(50),
        title VARCHAR(255) NOT NULL,
        body VARCHAR(255) NOT NULL,
        votes INT DEFAULT 0
    );'''
    print('Creating questions_table.....')

    comments_table = '''CREATE TABLE IF NOT EXISTS comments(
        id SERIAL PRIMARY KEY,
        created_by INTEGER NOT NULL REFERENCES users(id),
        created_on VARCHAR(50),
        comment VARCHAR(255) NOT NULL
    );'''
    print('Creating comments table....')

    rsvps_table = ''' CREATE TABLE IF NOT EXISTS rsvps(
        id SERIAL PRIMARY KEY,
        created_by INTEGER NOT NULL REFERENCES users(id),
        meetup_id INT NOT NULL,
        response VARCHAR(255)
    );'''
    print('Creating rsvps table....')

    tables = [users_table, meetups_table,
              questions_table, comments_table, rsvps_table]

    return tables