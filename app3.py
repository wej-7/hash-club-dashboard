import streamlit as st
import pandas as pd
import plotly.express as px
import os

# إعداد صفحة لوحة التحكم
st.set_page_config(page_title="لوحة مؤشرات أداء نادي هاش", page_icon="📊", layout="wide")

# اسم الصورة المعتمد لديك
IMAGE_FILENAME = "12.jpg"

# عرض الصورة في أعلى اللوحة
try:
    if os.path.exists(IMAGE_FILENAME):
        st.image(IMAGE_FILENAME, use_container_width=True)
    else:
        st.error(f"الصورة باسم '{IMAGE_FILENAME}' غير موجودة في مجلد المشروع.")
except Exception as e:
    st.markdown("<h1 style='text-align: center; color: #0EA5E9;'>نادي هاش | Hash Club</h1>", unsafe_allow_html=True)

st.markdown("---")

# الشريط الجانبي للتنقل والتصفية
st.sidebar.header("لوحة التحكم")
selected_category = st.sidebar.selectbox(
    "فلترة البيانات حسب الفئة:",
    ["الكل", "المتقدمين لعضوية النادي", "المتابعين للحساب الرسمي", "النخبة من المقبولين", "مخرجات النادي", "المشاهدات", "المناطق داخل وخارج المملكة"]
)
st.sidebar.markdown("---")
st.sidebar.text("نظام متابعة وتطوير الأداء")

# عنوان اللوحة الرئيسي مع النص الأصلي المطلوب
st.markdown("<h2 style='text-align: center; color: #0EA5E9;'>إحصائيات ومؤشرات الأداء</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8;'>متابعة حية لمخرجات ونمو النادي الرقمي</p>", unsafe_allow_html=True)
st.markdown("---")

# قاعدة البيانات المحدثة بناءً على التصميم المطلوب
data = {
    'فئة الإحصائية': [
        'المتقدمين لعضوية النادي', 
        'المتابعين للحساب الرسمي', 
        'النخبة من المقبولين', 
        'مخرجات النادي', 
        'المشاهدات', 
        'المناطق داخل وخارج المملكة'
    ],
    'القيمة المعروضة': ['+2000', '+1.3K', '+170', '+23', '+100K', '+20'],
    'القيمة العددية': [2000, 1300, 170, 23, 100000, 20],
    'التصنيف': ['عضوية', 'جمهور', 'نخبة', 'مشاريع', 'تفاعل', 'نطاق']
}
df = pd.DataFrame(data)

# تصفية البيانات
if selected_category != "الكل":
    display_df = df[df['فئة الإحصائية'] == selected_category]
else:
    display_df = df

# تقسيم الشاشة: الرسم البياني التفاعلي + البطاقات التفصيلية
col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("التحليل البصري للإحصائيات")
    fig = px.bar(
        display_df, 
        x='فئة الإحصائية', 
        y='القيمة العددية', 
        color='فئة الإحصائية',
        color_discrete_sequence=['#0EA5E9', '#38BDF8', '#0284C7', '#0369A1', '#38BDF8', '#0EA5E9'],
        text='القيمة المعروضة'
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis_title="",
        yaxis_title="القيمة"
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with col_right:
    st.subheader("البطاقات التفصيلية للسجلات")
    
    # عرض البيانات على شكل بطاقات رسمية مطابقة للتصميم تماماً
    for index, row in display_df.iterrows():
        st.markdown(f"""
        <div style='background-color: #1e293b; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #0EA5E9;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <span style='color: #38BDF8; font-weight: bold; font-size: 14px;'>{row['فئة الإحصائية']}</span>
                <span style='background-color: #0f172a; color: #94A3B8; padding: 2px 6px; border-radius: 4px; font-size: 10px;'>{row['التصنيف']}</span>
            </div>
            <div style='color: #ffffff; font-size: 18px; font-weight: bold; margin-top: 4px;'>{row['القيمة المعروضة']}</div>
        </div>
        """, unsafe_allow_html=True)
