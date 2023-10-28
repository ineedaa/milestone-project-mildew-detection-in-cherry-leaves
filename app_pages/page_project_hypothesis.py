import streamlit as st 


def page_project_hypothesis_body():

    st.header("Mildew Detection in Cherry Leaves Hypothesis")

    st.info(
        f"There are 4 main hypotheses for this project:\n\n "

        f"* 1 - Cherry Leaves infected with powdery mildew have white blotches, white streaks and fuzzy white surface  "
        f"    making them appear significantly different than healthy Cherry leaves.\n" 
        f"* 2 - The ML image visualizer app will be able to differentiate between a healthy cherry leaf and an "
        f"    infected cherry leaf with at least 97% accuracy.\n"
        f"* 3 - The ML image visualizer app can help decrease the amount of time needed to differentiate between "
        f"    the images thereby saving the employee and company both time and money during the inspection process.\n"
        f"* 4 - Validation of the image visualizer app will come from the the ML pipeline performance of the validation "
        f"    and test set differentiating between an infected leaf and and a healthy leaf with at least 97% accuracy.\n\n"
    )

    st.success(
        f"Images of healthy leaves will present darker green colors, while infected leaves will present lighter "
        f"colours, white streaks, white blotches and white fuzzy surfaces.\n\n"
        f"The ML image validator app will differentiate between a healthy Cherry Leaf and an infected leaf.\n"
        f"The ML image validator app will prove to be at least 97% accurate in the training, and validating trials.\n\n"
        f"Select the Cherry Leaf Visualizer page in the sidebar for an image montage of healthy and infected leaves."
    )