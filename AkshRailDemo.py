import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import numpy as np
import plotly.express as px

# ---------- Function to load Lottie animation ----------
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------- Load Logo ----------
# Assuming the logo path is correctly set or removed for a placeholder if not found
try:
    logo = Image.open("Screenshot (4).png")
except FileNotFoundError:
    st.warning("Logo file not found. Using a placeholder or removing logo for now.")
    logo = None # Set to None if file not found

# Page Config
st.set_page_config(page_title="AkshRail", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    .css-1d391kg { /* sidebar */
        background-color: #f0f2f6;
    }
    .css-1oe5zmf { /* main app background */
        background-color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #333366; /* Dark blue for headers */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green button */
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stAlert {
        border-left: 6px solid #2196F3; /* Blue alert border */
        background-color: #66bde8;
    }
    .stExpander {
        border: 1px solid #ddd;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    /* Metric styling */
    div[data-testid="stMetricValue"] {
        font-size: 36px;
        color: #007bff; /* Blue for metric values */
    }
    div[data-testid="stMetricLabel"] {
        font-size: 18px;
        color: #555;
    }
    div[data-testid="stSidebar"] {
        background-image: linear-gradient(to bottom, #333366, #5C5C8A); /* Gradient sidebar */
        color: white;
    }
    div[data-testid="stSidebar"] .stRadio > label {
        color: white;
    }
    div[data-testid="stSidebar"] .stTitle {
        color: white;
    }
</style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([1, 5])
with col1:
    if logo:
        st.image(logo, width=180)
    else:
        st.markdown("<h1 style='color: #333366;'>🚆</h1>", unsafe_allow_html=True) # Placeholder icon
with col2:
    st.title(" AkshRail")
    st.subheader("Where Information Meets Action")
    st.markdown("---") # Visual separator

# ---------- Sidebar ----------
st.sidebar.title("📂 Navigation")
st.sidebar.markdown("---")
menu = st.sidebar.radio("Go to:", ["Home", "Dashboard", "Upload", "Search", "Analytics", "About"])
st.sidebar.markdown("---")
st.sidebar.info("Developed for Kochi Metro Rail Limited")


# ---------- Lottie Animations (Centralized) ----------
# Ensure these URLs are stable or provide fallback
home_lottie = load_lottie_url("https://lottie.host/17eb65e5-3375-4c07-a50d-d1235b62b32f/lQ2Jz8wO9D.json") # Welcome
summary_lottie = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_u4yrau.json")  # AI Animation
alert_lottie = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_tutvdkg0.json")  # Alert/Notification
upload_lottie = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_jbr3byh0.json") # Upload
search_lottie = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_x17yudbs.json") # Search
analytics_lottie = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_mhlvj87g.json") # Analytics
about_lottie = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_tpgx4e3e.json") # About/Info


# ---------- HOME PAGE ----------
if menu == "Home":
    st.header("Welcome to AkshRail")
    st.markdown("### Intelligent Document Management for Kochi Metro Rail")

    col_lottie, col_text = st.columns([1, 2])
    with col_lottie:
        if home_lottie:
            st_lottie(home_lottie, height=250, key="home_welcome")
    with col_text:
        st.write("""
        AkshRail is an **AI-powered solution** designed to revolutionize document management for Kochi Metro Rail Limited.
        Say goodbye to manual filing and hello to automated summaries, intelligent search, and actionable insights.
        """)
        st.info("Our mission: To transform document overload into a streamlined, efficient information hub.")

    st.markdown("---")
    st.subheader("🚀 Core Capabilities")
    col_cap1, col_cap2, col_cap3 = st.columns(3)
    with col_cap1:
        st.markdown("#### OCR & Text Extraction")
        st.markdown("Extracts text from scanned PDFs, images, and various document formats with high accuracy.")
    with col_cap2:
        st.markdown("#### NLP for Insights")
        st.markdown("Summarizes content, identifies key entities, and detects duplicates using advanced Natural Language Processing.")
    with col_cap3:
        st.markdown("#### Smart Search & Linkage")
        st.markdown("Provides blazing-fast search capabilities and automatically links related documents for comprehensive understanding.")

    st.markdown("---")

    st.subheader("💡 Technologies & Functions Overview")
    with st.expander("Explore Technologies Used"):
        st.write("""
        - **OCR (Optical Character Recognition):** Leverages Tesseract or cloud-based OCR services to convert scanned documents into editable and searchable text.
        - **NLP (Natural Language Processing):** Utilizes libraries like **SpaCy** for entity recognition and summarization, and potentially **Hugging Face Transformers** for more advanced contextual understanding and duplicate checking.
        - **ElasticSearch:** A powerful, distributed search and analytics engine for storing, indexing, and enabling lightning-fast searches across all documents. Also used for creating semantic links between documents.
        - **Database (PostgreSQL/MongoDB):** **PostgreSQL** for structured metadata (document IDs, upload dates, user info) and **MongoDB** for flexible storage of document content and processed NLP data.
        - **Backend (Flask/Django):** A robust **Flask** API handles document uploads, OCR processing, NLP tasks, database interactions, and pushes notifications.
        - **Frontend (Streamlit/React):** **Streamlit** for the interactive, staff-friendly dashboards and **React** (if a more complex, scalable web app is needed later) for richer UI/UX.
        - **Multi-language Support:** Integration with NLP models capable of processing **English & Malayalam** text.
        """)
    with st.expander("🛠️ Methodology (Stepwise)"):
        st.write("""
        1. **Document Upload:** Staff uploads documents (PDF/TXT/Scans) via a secure web interface.
        2. **Text Extraction (OCR):** Scanned documents undergo OCR to extract text content, which is then cleaned and pre-processed.
        3. **Processing & Summarization (NLP):** Extracted text is fed into NLP pipelines for summarization, keyword extraction, and identifying potential duplicates.
        4. **Smart Storage & Search (ElasticSearch & DB):** Documents and their metadata (summaries, keywords, entities) are indexed in ElasticSearch and stored in the database for efficient retrieval and linking.
        5. **Alerts & Dashboards:** Role-based dashboards provide staff with an overview, and a notification system delivers critical updates and alerts.
        """)

    
    with st.expander("🌟 How it Differs from Current Metro System"):
        st.write("""
         - Current system relies heavily on **manual reading and filing**, leading to inefficiencies.
        - AkshRail automatically **summarizes, searches, and intelligently links documents**, saving countless hours.
         - Provides **role-specific dashboards** for tailored information access.
         - Offers robust **multi-language support** (English & Malayalam) for broader usability.
         - Implements smart **alerts & notifications** for critical updates and deadlines.
            """)

    with st.expander("✅ Key Benefits"):
        st.write("""
            - **Saves significant time**: Quick access to summaries and search results.
            - **Improves teamwork & collaboration**: Centralized, easily searchable access for all authorized staff.
            - **Ensures compliance**: Highlights critical updates and policy changes.
            - **Reduces duplicated effort**: Automatic duplicate detection and summaries prevent redundant work.
            - **Preserves institutional knowledge**: Creates a living archive of company documents and insights.
            - **Enhances decision-making**: Provides data-driven insights from document analytics.
            """)

# ---------- DASHBOARD ----------
elif menu == "Dashboard":
    st.subheader("📊 AkshRail Dashboard")
    st.info("Your main control center: Get an overview of document activity, pending tasks, and system health.")

    col_metrics, col_lottie_dash = st.columns([2, 1])
    with col_metrics:
        # Improved Metrics with custom colors
        st.markdown(
            """
            <style>
            .metric-box {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 15px;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            }
            .metric-label {
                font-size: 16px;
                color: #555;
            }
            .metric-value {
                font-size: 32px;
                font-weight: bold;
                color: #007bff; /* Primary blue */
            }
            </style>
            """, unsafe_allow_html=True
        )

        st.markdown('<div class="metric-box"><div class="metric-label">Total Documents Indexed</div><div class="metric-value">1,245</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-box"><div class="metric-label">Documents Awaiting Review</div><div class="metric-value">37</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="metric-box"><div class="metric-label">New Uploads This Month</div><div class="metric-value">223</div></div>', unsafe_allow_html=True)

    with col_lottie_dash:
        if alert_lottie:
            st_lottie(alert_lottie, height=200, key="dashboard_alert_lottie")
        st.markdown("---")
        st.markdown("#### Quick Actions")
        if st.button("Review Pending Documents"):
            st.session_state.menu = "Search" # Example of changing menu based on action
            st.experimental_rerun()
        if st.button("Upload New Document"):
            st.session_state.menu = "Upload"
            st.experimental_rerun()


    st.markdown("---")
    st.subheader("Recent Document Activity")
    # Sample Data for a table/chart
    activity_data = {
        "Document ID": ["DOC-1023", "DOC-2087", "DOC-1150", "DOC-0998", "DOC-3011"],
        "Title": ["Maintenance Schedule Q3", "Vendor Invoice #4567", "Safety Protocol Update", "Board Meeting Minutes", "New Project Proposal"],
        "Type": ["Report", "Invoice", "Policy", "Minutes", "Proposal"],
        "Last Modified": ["2023-10-26", "2023-10-25", "2023-10-24", "2023-10-23", "2023-10-22"],
        "Status": ["Approved", "Pending Payment", "Under Review", "Finalized", "Draft"]
    }
    df_activity = pd.DataFrame(activity_data)
    st.dataframe(df_activity)

    st.markdown("---")
    st.subheader("Document Type Distribution")
    type_counts = df_activity["Type"].value_counts().reset_index()
    type_counts.columns = ["Document Type", "Count"]
    fig_pie = px.pie(type_counts, values='Count', names='Document Type', title='Distribution by Document Type',
                     color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pie, use_container_width=True)

    with st.expander("🛠️ Functions and Technologies on Dashboard"):
        st.write("""
        - **Metrics & KPIs:** Displays key performance indicators from the database (PostgreSQL/MongoDB) like total documents, pending reviews, calculated by aggregation queries.
        - **Lottie Animations:** Uses `streamlit_lottie` to display dynamic alerts and notifications.
        - **Data Table (`st.dataframe`):** Fetches recent document activity from ElasticSearch/Database and displays it in an interactive table.
        - **Pie Chart (`plotly.express`):** Visualizes the distribution of document types based on aggregated data from the document repository, providing quick insights.
        - **Interactive Buttons:** Allows direct navigation to other sections (e.g., "Upload") to streamline workflows.
        """)

# ---------- UPLOAD ----------
elif menu == "Upload":
    st.subheader("📤 Upload New Documents to AkshRail")
    st.info("Effortlessly upload engineering drawings, invoices, reports, and various other document types. Our system will automatically process them.")

    col_upload_form, col_upload_lottie = st.columns([2, 1])
    with col_upload_form:
        with st.form("document_upload_form"):
            uploaded_file = st.file_uploader("Choose a document to upload", type=["pdf", "docx", "jpg", "png", "txt", "xlsx"], help="Supported formats: PDF, DOCX, JPG, PNG, TXT, XLSX")
            document_title = st.text_input("Document Title (Optional)", placeholder="e.g., Q4 Financial Report, Metro Line 3 Design")
            document_type = st.selectbox("Document Type", ["Report", "Invoice", "Drawing", "Policy", "Minutes", "Legal", "Other"], index=0)
            submit_button = st.form_submit_button("Upload Document & Process")

            if submit_button:
                if uploaded_file is not None:
                    st.success(f"✅ Document '{uploaded_file.name}' uploaded successfully!")
                    st.write("Processing document...")
                    with st.spinner("Extracting text, generating summary, and indexing..."):
                        # Simulate processing time
                        import time
                        time.sleep(3)
                    st.success("Document processed and indexed!")
                    st.markdown(f"**Title:** {document_title if document_title else uploaded_file.name}")
                    st.markdown(f"**Type:** {document_type}")
                    st.markdown("A summary and relevant links will be available in the Search section shortly.")
                else:
                    st.error("Please select a file to upload.")

    with col_upload_lottie:
        if upload_lottie:
            st_lottie(upload_lottie, height=300, key="upload_animation")
        st.markdown("---")
        st.markdown("#### How it Works:")
        st.write("""
        1. **Upload:** Your file is securely transmitted.
        2. **OCR:** If it's an image/scanned PDF, text is extracted.
        3. **NLP:** Content is analyzed, summarized, and keywords are identified.
        4. **Indexing:** The document and its metadata are stored in ElasticSearch for rapid retrieval.
        """)

    with st.expander("🛠️ Functions and Technologies on Upload Page"):
        st.write("""
        - **File Uploader (`st.file_uploader`):** Handles secure file uploads from the user interface.
        - **Forms (`st.form`):** Organizes user input fields for metadata (title, type) and streamlines submission.
        - **Backend Integration (Simulated):** In a real application, the `submit_button` would trigger an API call to a **Flask/Django** backend.
        - **OCR & NLP (Backend):** The backend would then initiate **OCR (e.g., Tesseract, Google Cloud Vision)** for scanned documents and **NLP (SpaCy, Hugging Face)** for summarization and entity extraction.
        - **Database & ElasticSearch (Backend):** The processed data would be stored in **PostgreSQL/MongoDB** and indexed in **ElasticSearch** for search functionality.
        - **Streamlit Spinners (`st.spinner`):** Provides visual feedback during backend processing.
        """)


# ---------- SEARCH ----------
elif menu == "Search":
    st.subheader("🔍 Smart Search & Retrieve Documents")
    st.info("Find any document instantly with advanced search capabilities. Use keywords, document IDs, or even natural language queries.")

    col_search_input, col_search_lottie = st.columns([2, 1])
    with col_search_input:
        query = st.text_input("Enter keywords, document ID, or a natural language query:", placeholder="e.g., 'Maintenance report Q3', 'invoice from ABC Corp', 'Safety guidelines'")
        col_search_btn, col_search_filter = st.columns([1, 1])
        with col_search_btn:
            search_button = st.button("Perform Smart Search")
        with col_search_filter:
            document_type_filter = st.multiselect("Filter by Document Type", ["Report", "Invoice", "Drawing", "Policy", "Minutes", "Legal", "Other"], default=[])

    with col_search_lottie:
        if search_lottie:
            st_lottie(search_lottie, height=200, key="search_animation")

    st.markdown("---")

    if search_button and query:
        st.success(f"Searching for: **'{query}'** (Filters: {', '.join(document_type_filter) if document_type_filter else 'None'})")
        with st.spinner("Retrieving results from ElasticSearch..."):
            import time
            time.sleep(2) # Simulate search time

        # Sample search results
        results_data = {
            "Document ID": ["DOC-1023", "DOC-2087", "DOC-1150", "DOC-0998"],
            "Title": ["Metro Line 1 Maintenance Report Q3 2023", "Invoice ABC Corp #4567 for Q2", "Updated Safety Protocol for Station Operations", "October Board Meeting Minutes"],
            "Type": ["Report", "Invoice", "Policy", "Minutes"],
            "Relevance Score": [0.95, 0.88, 0.82, 0.75],
            "Preview": ["Summary: Overview of routine maintenance tasks...", "Summary: Details of materials supplied by...", "Summary: New guidelines for emergency...", "Summary: Key decisions on budget allocation..."],
            "Link": ["View DOC-1023", "View DOC-2087", "View DOC-1150", "View DOC-0998"]
        }
        df_results = pd.DataFrame(results_data)

        # Apply simple filter for demonstration
        if document_type_filter:
            df_results = df_results[df_results["Type"].isin(document_type_filter)]

        if not df_results.empty:
            st.subheader("Search Results")
            for index, row in df_results.iterrows():
                st.markdown(f"#### {row['Title']} (ID: {row['Document ID']})")
                st.markdown(f"**Type:** {row['Type']} | **Relevance:** {row['Relevance Score']:.0%}")
                with st.expander("Read Preview"):
                    st.write(row['Preview'])
                st.button(row['Link'], key=f"view_{row['Document ID']}")
                st.markdown("---")
        else:
            st.warning("No documents found matching your query and filters.")
    elif search_button:
        st.warning("Please enter a search query.")

    with st.expander("🛠️ Functions and Technologies on Search Page"):
        st.write("""
        - **Text Input & Buttons (`st.text_input`, `st.button`):** User interface for entering search queries and initiating searches.
        - **Multi-select Filter (`st.multiselect`):** Allows users to refine searches by document type.
        - **ElasticSearch (Backend):** This is the core technology. When a query is submitted, it's sent to the **ElasticSearch** index.
            - **Full-Text Search:** ElasticSearch performs fast and relevant full-text searches on document content and summaries.
            - **Faceted Search:** Filters by document type are handled efficiently by ElasticSearch's aggregation capabilities.
            - **Semantic Search (NLP):** If the query involves natural language, NLP models (e.g., **Hugging Face sentence transformers**) can convert the query into an embedding, which ElasticSearch then uses for vector similarity search to find semantically similar documents.
        - **Relevance Ranking:** ElasticSearch provides relevance scores to order results.
        - **Backend API (Flask/Django):** Handles the communication between Streamlit and ElasticSearch, processes queries, and formats results.
        """)

# ---------- ANALYTICS ----------
elif menu == "Analytics":
    st.subheader("📈 Analytics & Insights")
    st.info("Unlock meaningful insights from your document data. Visualize trends, identify bottlenecks, and monitor system usage.")

    if analytics_lottie:
        st_lottie(analytics_lottie, height=200, key="analytics_animation")
    st.markdown("---")

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.markdown("#### Monthly Document Uploads")
        # Generate some sample data for uploads
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
        uploads = np.random.randint(150, 300, size=len(months))
        df_uploads = pd.DataFrame({"Month": months, "Uploads": uploads})
        fig_uploads = px.line(df_uploads, x="Month", y="Uploads", markers=True,
                              title="Monthly Document Upload Trend",
                              labels={"Uploads": "Number of Documents"},
                              color_discrete_sequence=["#1f77b4"]) # Blue line
        st.plotly_chart(fig_uploads, use_container_width=True)

    with col_chart2:
        st.markdown("#### Document Status Distribution")
        # Generate sample data for status
        status_data = pd.DataFrame({
            "Status": ["Approved", "Pending Review", "Draft", "Archived", "Rejected"],
            "Count": [500, 120, 80, 400, 20]
        })
        fig_status = px.bar(status_data, x="Status", y="Count",
                            title="Current Document Status",
                            color="Status",
                            color_discrete_sequence=px.colors.qualitative.G10) # Colorful bars
        st.plotly_chart(fig_status, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Top 5 Most Searched Keywords")
    # Sample data for keywords
    keywords_data = {
        "Keyword": ["Metro Line Expansion", "Safety Audit", "Vendor Contract", "Financial Report Q3", "Daily Operations"],
        "Search Count": [150, 120, 90, 80, 75]
    }
    df_keywords = pd.DataFrame(keywords_data)
    fig_keywords = px.bar(df_keywords.sort_values("Search Count", ascending=True),
                          x="Search Count", y="Keyword", orientation='h',
                          title="Most Frequent Search Terms",
                          color_discrete_sequence=["#2ca02c"]) # Green bars
    st.plotly_chart(fig_keywords, use_container_width=True)

    with st.expander("🛠️ Functions and Technologies on Analytics Page"):
        st.write("""
        - **Data Aggregation (Backend & Database/ElasticSearch):** Analytics charts are powered by aggregated data from **PostgreSQL/MongoDB** (for structured metadata) and **ElasticSearch** (for operational metrics like search counts).
        - **Plotly Express (`plotly.express`):** Used for creating interactive and visually rich charts:
            - **Line Charts:** For showing trends over time (e.g., monthly uploads).
            - **Bar Charts:** For comparing categories (e.g., document status, top keywords).
            - **Pie Charts (on Dashboard):** For showing distribution.
        - **Data Processing (Pandas):** Data fetched from the backend is processed and formatted using **Pandas DataFrames** before being visualized.
        - **Backend Analytics Engine (Flask/Django):** A dedicated backend service calculates and provides the aggregated data required for these visualizations.
        """)

# ---------- ABOUT ----------
elif menu == "About":
    st.subheader("ℹ️ About AkshRail: Powering Kochi Metro's Future")
    st.write("AkshRail is a brainchild developed to tackle the challenges of document overload and information fragmentation at Kochi Metro Rail Limited.")

    col_about_text, col_about_lottie = st.columns([2, 1])
    with col_about_text:
        st.markdown("#### Our Vision")
        st.write("To establish a seamless, intelligent, and accessible document management ecosystem that enhances operational efficiency, fosters collaboration, and safeguards critical organizational knowledge for Kochi Metro.")
        st.markdown("#### The Team")
        st.write("This solution is developed by a dedicated team with expertise in AI, web development, and data management, committed to delivering a robust and user-friendly system.")
        st.markdown("#### Get in Touch")
        st.write("For support, feedback, or further inquiries, please contact our development team.")
        st.markdown("---")
        st.markdown("🚀 Built with passion using:")
        st.markdown("""
        - **Python:** The backbone of our AI and backend logic.
        - **Streamlit:** For creating beautiful and interactive web applications with ease.
        - **Flask/Django:** Robust backend frameworks for API development and task management.
        - **AI (NLP & OCR):** The intelligence that powers summarization, search, and data extraction.
        - **ElasticSearch:** For lightning-fast, intelligent search and document indexing.
        - **PostgreSQL/MongoDB:** Reliable databases for structured and unstructured data storage.
        - **Cloud Storage:** For scalable and secure document storage (e.g., AWS S3, Google Cloud Storage).
        """)

    with col_about_lottie:
        if about_lottie:
            st_lottie(about_lottie, height=300, key="about_animation")

    st.markdown("---")
    st.write("© 2025 AkshRail. All rights reserved.")


