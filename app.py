
import streamlit as st
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="근골격계 부담작업 체크리스트", layout="wide")

st.title("💪 근골격계 부담작업 체크리스트")

# 기본 정보 입력
st.subheader("🗂️ 기본 정보 입력")
company = st.text_input("회사명")
department = st.text_input("부서명")
work_name = st.text_input("작업명")
unit_work = st.text_input("단위작업명")
work_time = st.text_input("작업시간 (예: 8시간)")
total_weight = st.text_input("총 물량 (Kg)")
date = st.date_input("작업일자", value=datetime.date.today())

# 항목 정의
items = {
    1: "하루 4시간 이상 키보드 또는 마우스를 조작하는 작업",
    2: "2시간 이상 같은 동작을 반복하는 작업",
    3: "팔을 어깨 위로 드는 작업 등",
    4: "목이나 허리를 구부리거나 트는 작업",
    5: "쪼그리거나 무릎을 굽힌 자세의 작업",
    6: "손가락으로 1kg 이상을 집는 작업",
    7: "한 손으로 4.5kg 이상 드는 작업",
    8: "25kg 이상 물체를 하루 10회 이상 드는 작업",
    9: "10kg 이상 물체를 무릎 아래, 어깨 위 등에서 드는 작업",
    10: "4.5kg 이상 물체를 분당 2회 이상 드는 작업",
    11: "손 또는 무릎으로 반복 충격을 가하는 작업",
    12: "기타 신체에 부담을 주는 작업"
}

st.subheader("✅ 부담작업 항목 체크")
responses = []
for i in range(1, 13):
    st.markdown(f"**{i}호. {items[i]}**")
    selected = st.radio(f"{i}호 작업 해당 여부", ["예", "아니오"], key=f"item_{i}")
    count = st.number_input(f"해당 인원 수 (명)", min_value=0, step=1, key=f"count_{i}")
    memo = st.text_input(f"메모 또는 작업 내용 (선택)", key=f"memo_{i}")
    responses.append((selected, count, memo))

# 작업내용 서술
st.subheader("📝 작업내용 서술")
num_rows = st.number_input("작성할 행 수 선택", min_value=1, max_value=10, value=1)
descriptions = []
for i in range(num_rows):
    desc = st.text_area(f"작업내용 {i+1}", key=f"desc_{i}")
    descriptions.append(desc)

# 저장 버튼
if st.button("✅ 제출 및 저장"):
    st.success("데이터가 제출되었습니다. (Google Sheets 연동은 별도 설정 필요)")
    st.write("입력된 데이터 요약:")
    st.write({
        "회사명": company, "부서명": department, "작업명": work_name,
        "단위작업명": unit_work, "작업시간": work_time, "총물량": total_weight,
        "작업일자": date
    })
    for i, (sel, cnt, mem) in enumerate(responses, start=1):
        st.write(f"{i}호 → 해당: {sel}, 인원: {cnt}, 메모: {mem}")
    for i, d in enumerate(descriptions, start=1):
        st.write(f"작업내용 {i}: {d}")
