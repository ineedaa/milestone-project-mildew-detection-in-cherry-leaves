import streamlit as st


def page_project_summary_body():

    st.title("Project Summary Overview")

    st.header("General Information: ")
    st.info(
        f"Cherry Leaves are an integral ingredient found in numerous products world wide, making them a big business "
        f"depending on how they are used. Cherry Leaves can be found in anything from Tea, to skin care products; as "
        f"well as over the counter vitamins and they are even used to help boost testosterone and cleanse the liver "
        f"However, as a naturally biological product, Cherry Trees and the leaves are subject to fungal infections, such as "
        f"Powdery Mildew.\n\n" 
        f"According to [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew), the ascomycete fungi "
        f"attacks and infects the lower leaves in more humid climates with devestating effects on the life of the  "
        f"host plant reducing plant harvest and other future harm. Healthy tree cellss are darker in colour as that aids "
        f"the photosynthesis process of trapping light; the powdery mildew leaves change the pigment of the tree leaf cells, "
        f"inhibiting the tree's ability to take in light and to photosynthesize light into energy which directly impacts "
        f"the tree's ability to grow and thrive as a living organism. The fungi spores spread with air movement making "
        f"fungal transmission multi-vectoral and therefore vital to quickly identify infected leaves and treat them "
        f"preventing the infection from causing further damage.\n\n"
    )

    if st.checkbox("Problem Statement:"):
        st.info(
            f"Farmy and Foods agricultural plantation has recently discovered Powdery Mildew infections in some of "
            f"their Cherry Trees. The Cherry Leaves production is one of their largest portfolio assets and there "
            f"can be a large financial short term and long term to a variety of thier crops if the infection is not "
            f"identified and prevented quickly. With conventional means, there is a large labor cost in time and resources "
            f"to identify infected leaves. Farmy and Foods requires a new method to quickly identify infected leaves "
            f"from healthy leaves in order to save time and labour to treat the trees, save the harvest and protect the "
            f"company's finances.\n\n"
            f"The [Kaggle Cherry Leaves](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) dataset contains "
            f"4208 images of healthy and infected cherry leaves and was used as the source to train the ML app.\n\n"
        )

    st.write(
        f"A visual comparison machine learning (ML) tool will enable employees throughout the company's vast properties "
        f"to quickly upload images fo Cherry Tree leaves to determine if they are infected or not. This ML tool "
        f"will be at least 97% accurate and significantly faster than the previous manual procedure. This ML tool will "
        f"save the company time, money, resources and labour; thus positively  impacting the financial outcome of the harvest.\n\n"
    )

    st.header("Business Requirements: ")
    if st.checkbox("Requirement 1:"):
        st.info(
            f"The study includes analysis on: "
            f" - average images and variability images for each class (healthy or powdery mildew).\n"
            f" - the differences between average healthy and average powdery mildew cherry leaves.\n"
            f" - an image montage for each class.\n"
        )

    if st.checkbox("Requirement 2:"):
        st.info(
            f"Deliver an ML system that is capable of predicting whether a cherry leaf is healthy or contains "
            f"powdery mildew based upon uploaded image comparrison to the learned AI app."
        )