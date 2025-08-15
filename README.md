# hospitalManagementSystem
A console-based Hospital Management System in Python with MySQL. Supports CRUD operations for patients, doctors, and appointments. Modular structure with database integration for easy management and scheduling.

<img width="468" height="276" alt="image" src="https://github.com/user-attachments/assets/d4686280-3763-4b75-963c-74855863bf4d" />


# Create a database in mysql commandline using following Commands:
CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    contact VARCHAR(15)
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    specialization VARCHAR(100),
    contact VARCHAR(15)
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);
