import cv2
import streamlit as st
import os

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def load_cascade_classifier():
    # Essayez de charger le classificateur en utilisant le chemin par défaut d'OpenCV
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    # Vérifiez si le classificateur est chargé correctement
    if face_cascade.empty():
        st.error("Erreur : Impossible de charger le classificateur Haar cascade.")
        return None
    return face_cascade

def detect_faces():
    # Charger le classificateur Haar cascade
    face_cascade = load_cascade_classifier()
   
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):  # check !
    # capture frame-by-frame
        ret, frame = cap.read()
        frame = cap.read()


        if ret: # check ! (some webcam's need a "warmup")
            # our operation on frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



        # Détecter les visages en utilisant le classificateur Haar Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)

        # Convertir l'image en RGB pour l'affichage dans Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Afficher l'image dans l'application Streamlit
    st.image(frame_rgb, caption="Détection de visages", use_column_width=True)

        # Sortir de la boucle si l'application est fermée
    if cv2.waitKey(1) & 0xFF == ord('q'):
            

    # Libérer la webcam
      cap.release()
      cv2.destroyAllWindows()

def app():
    st.title("Détection de visages avec l'algorithme de Viola-Jones")
    st.write("Appuyez sur le bouton ci-dessous pour commencer la détection des visages depuis votre webcam.")

    # Ajouter un bouton pour démarrer la détection des visages
    if st.button("Détecter les visages"):
        detect_faces()

if __name__ == "__main__":
    app()
