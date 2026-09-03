import pandas as pd
from app import app, db, Student

def seed_database():
    excel_path = 'St_Lawrence_Muwanga_S1_Term3_Register_System_v2.xlsx'
    df = pd.read_excel(excel_path, sheet_name='Student Bio Data', skiprows=5)
    
    with app.app_context():
        db.create_all()
        for _, row in df.iterrows():
            name = row.iloc[1]
            if pd.notna(name) and str(name).strip() != '':
                student_id = f"SLM-{row.iloc[0]:03d}"
                gender = str(row.iloc[2]) if pd.notna(row.iloc[2]) else 'M'
                
                student = Student(
                    student_id=student_id,
                    full_name=str(name).strip(),
                    gender=gender if gender in ['M', 'F'] else 'M',
                    student_class='S1'
                )
                db.session.merge(student)
        db.session.commit()
        print("Successfully seeded S.1 student register!")

if __name__ == '__main__':
    seed_database()