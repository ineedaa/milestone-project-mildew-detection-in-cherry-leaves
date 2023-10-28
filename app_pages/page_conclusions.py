import streamlit as st 


def page_conclusions_body():

    st.title("Project Conclusions: ")

    st.header("Hypothesis Outcomes:")
    if st.checkbox("Hypothesis 1:"):
        st.info(
            f"* 1 - Cherry Leaves infected with powdery mildew have white blotches, white streaks and fuzzy white surface  "
            f"making them appear significantly different than healthy Cherry leaves.\n\n"
            f"Proven Correct, the appearance of cherry leaves infected with powdery mildew are white in color and " 
            f"present as significantly different than a healthy cherry leaf. "
        )

    if st.checkbox("Hypothesis 2: "):
        st.write(
            f"* 2 - The ML image visualizer app will be able to differentiate between a healthy cherry leaf and an "
            f"infected cherry leaf with at least 97% accuracy.\n\n"
            f"Proven Correct, the ML Image Visualizer AI App was able to be trained to accurately predict "
            f"with greater than 97% accuracy, what the health status is of an unseen image of a cherry leaf"
        )

    if st.checkbox("Hypothesis 3: "):
        st.info(
            f"* 3 - The ML image visualizer app can help decrease the amount of time needed to differentiate between "
            f"the images thereby saving the employee and company both time and money during the inspection process.\n\n"
            f"Assumed Correct, until the app is put into the hands of the laborers in the feild, this hypothesis can only be "
            f"assumed to be correct. However, based on the present information and the time the app takes to predict "
            f"unseen images, it is a safe assumption that this hypothesis will be proven correct."
        )

    if st.checkbox("Hypothesis 4: "):
        st.write(
            f"* 4 - Validation of the image visualizer app will come from the the ML pipeline performance of the validation "
            f"and test set differentiating between an infected leaf and and a healthy leaf with at least 97% accuracy.\n\n"
            f"Proven Correct, the ML pipeline used for this project had an accuracy greater than 97% for all three training sets."
        )


    st.title("Project Outcomes:")

    st.header("Success")
    if st.checkbox("Business Requirement 1:"):
        st.success(
            f"The study includes analysis on: "
            f" - average images and variability images for each class (healthy or powdery mildew).\n"
            f" - the differences between average healthy and average powdery mildew cherry leaves.\n"
            f" - an image montage for each class.\n\n"

            f"Completed!"
        )

    if st.checkbox("Business Requirement 2:"):
        st.success(
            f"Deliver an ML system that is capable of predicting whether a cherry leaf is healthy or contains "
            f"powdery mildew based upon uploaded image comparison to the learned AI app.\n\n"

            f"Completed!"
        )

    if st.checkbox("Verification"):
        st.warning(
            f"In order to verify that this project and app can be successfully replicated with the same outcome, "
            f"the customer retaining the NDA contract and private information must be contacted and agree to "
            f"allow the replication process access to the notebooks and code for an attempt to replicate and "
            f"validate the outcome of this project."
        )