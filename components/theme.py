import streamlit as st


def apply_global_style():

    st.markdown(
        """
        <style>

        /* Global */

        .stApp {
            background-color: #F8FAFC;
            color: #0F172A;
            font-family: "Inter", "Segoe UI", sans-serif;
        }


        /* Remove default padding */

        .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }


        /* Main title */

        h1, h2, h3 {
            color: #0F172A;
            font-weight: 700;
        }


        /* Sidebar */

        section[data-testid="stSidebar"] {

            background-color: #0F172A;

        }


        section[data-testid="stSidebar"] * {

            color: white;

        }


        /* Cards */


        .sb-card {

            background: white;

            border-radius: 12px;

            padding: 20px;

            border: 1px solid #E5E7EB;

            box-shadow:
            0 1px 3px rgba(0,0,0,0.05);

            min-height:120px;

        }


        .sb-card-title {

            font-size:14px;

            color:#64748B;

            margin-bottom:8px;

        }


        .sb-card-value {

            font-size:32px;

            font-weight:700;

            color:#0F172A;

        }


        .sb-card-desc {

            font-size:13px;

            color:#16A34A;

        }


        /* Section */

        .section-title {

            font-size:20px;

            font-weight:700;

            margin-top:20px;

            margin-bottom:15px;

        }



        /* Status badge */


        .badge {

            padding:5px 10px;

            border-radius:20px;

            font-size:12px;

            font-weight:600;

        }


        .badge-success {

            background:#DCFCE7;

            color:#166534;

        }


        .badge-warning {

            background:#FEF3C7;

            color:#92400E;

        }


        .badge-danger {

            background:#FEE2E2;

            color:#991B1B;

        }


        </style>

        """,
        unsafe_allow_html=True
    )
