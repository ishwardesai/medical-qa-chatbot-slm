"""
Medical Knowledge Base
Contains the medical document corpus used for RAG retrieval.
"""

MEDICAL_DOCUMENTS = [
    {
        "id": 1,
        "title": "Hypertension",
        "content": (
            "Hypertension, or high blood pressure, is defined as systolic blood pressure "
            "above 130 mmHg or diastolic above 80 mmHg. It is a major risk factor for "
            "stroke, heart attack, and kidney disease. First-line treatments include "
            "lifestyle changes such as reducing sodium intake, regular exercise, and "
            "limiting alcohol. Medications include ACE inhibitors, ARBs, calcium channel "
            "blockers, and thiazide diuretics."
        )
    },
    {
        "id": 2,
        "title": "Type 2 Diabetes",
        "content": (
            "Type 2 diabetes is a chronic condition where the body becomes resistant to "
            "insulin or does not produce enough. Symptoms include increased thirst, frequent "
            "urination, fatigue, blurred vision, and slow-healing sores. Management involves "
            "blood sugar monitoring, healthy diet, regular exercise, and medications such as "
            "metformin. Regular HbA1c testing is recommended every 3 months."
        )
    },
    {
        "id": 3,
        "title": "Asthma",
        "content": (
            "Asthma is a chronic inflammatory disease of the airways causing variable airflow "
            "obstruction and bronchial hyperresponsiveness. Triggers include allergens, "
            "exercise, cold air, respiratory infections, and air pollutants. Symptoms include "
            "wheezing, shortness of breath, chest tightness, and cough. Treatment uses "
            "short-acting beta-agonists for rescue and inhaled corticosteroids for long-term "
            "control."
        )
    },
    {
        "id": 4,
        "title": "Myocardial Infarction",
        "content": (
            "Myocardial infarction, or heart attack, occurs when blood flow to part of the "
            "heart muscle is blocked, causing tissue death. The most common cause is rupture "
            "of an atherosclerotic plaque in a coronary artery. Symptoms include severe chest "
            "pain radiating to the left arm or jaw, diaphoresis, nausea, and dyspnea. "
            "Immediate treatment includes aspirin, anticoagulation, and primary percutaneous "
            "coronary intervention."
        )
    },
    {
        "id": 5,
        "title": "Pneumonia",
        "content": (
            "Pneumonia is an infection of the lung parenchyma caused by bacteria, viruses, "
            "or fungi. Streptococcus pneumoniae is the most common bacterial cause in adults. "
            "Symptoms include fever, productive cough, pleuritic chest pain, and dyspnea. "
            "Severity is assessed using the CURB-65 score. Community-acquired pneumonia is "
            "treated with amoxicillin or a macrolide antibiotic for mild cases."
        )
    },
    {
        "id": 6,
        "title": "Depression",
        "content": (
            "Depression is a mood disorder characterized by persistent sadness, loss of "
            "interest, and impaired daily functioning lasting at least two weeks. Core "
            "symptoms include depressed mood, anhedonia, fatigue, difficulty concentrating, "
            "and suicidal ideation. Diagnosis uses DSM-5 criteria. Treatment includes "
            "cognitive behavioral therapy and SSRIs as first-line antidepressants."
        )
    },
    {
        "id": 7,
        "title": "Stroke",
        "content": (
            "Stroke occurs when blood supply to part of the brain is cut off, causing brain "
            "cells to die. Ischemic stroke accounts for 87% of cases and is caused by a "
            "blood clot blocking an artery. FAST acronym: Face drooping, Arm weakness, "
            "Speech difficulty, Time to call emergency services. Treatment for ischemic "
            "stroke includes tPA within 4.5 hours of onset."
        )
    },
    {
        "id": 8,
        "title": "COPD",
        "content": (
            "Chronic obstructive pulmonary disease is a chronic inflammatory lung disease "
            "causing obstructed airflow. The primary cause is long-term exposure to "
            "irritating gases, most often cigarette smoke. Symptoms include breathing "
            "difficulty, cough, mucus production, and wheezing. Diagnosis is confirmed "
            "by spirometry. Smoking cessation is the most important intervention to slow "
            "disease progression."
        )
    },
    {
        "id": 9,
        "title": "Sepsis",
        "content": (
            "Sepsis is a life-threatening emergency caused by the body's extreme response "
            "to an infection. Symptoms include fever or low temperature, rapid heart rate, "
            "rapid breathing, confusion, and organ dysfunction. The Sepsis Six bundle "
            "includes oxygen, blood cultures, IV antibiotics, IV fluids, lactate "
            "measurement, and urine output monitoring. Early treatment within the golden "
            "hour significantly improves survival."
        )
    },
    {
        "id": 10,
        "title": "Parkinson's Disease",
        "content": (
            "Parkinson's disease is a progressive nervous system disorder affecting "
            "movement. It results from the loss of dopamine-producing neurons in the "
            "substantia nigra. Symptoms include tremor at rest, rigidity, bradykinesia, "
            "and postural instability. Treatment includes levodopa/carbidopa as the most "
            "effective medication, dopamine agonists, and deep brain stimulation for "
            "advanced cases."
        )
    },
]
