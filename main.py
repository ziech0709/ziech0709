import streamlit as st

# HTML로 블리치 스타일 배경화면 설정
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2k0Loeokxtp362LKQpPuKXE6L9FAONlgjGQ&s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

# Streamlit 앱에 스타일 적용
st.markdown(page_bg_img, unsafe_allow_html=True)

# 웹사이트 제목
st.title("블리치(ブリーチ)(BLEACH) - 만화 소개")

# 제목 아래에 블리치 메인 이미지 추가
st.image(
    "https://i.ytimg.com/vi/gqOg84UYQoA/maxresdefault.jpg",
    caption="BLEACH 20주년 기념 이미지",
    use_column_width=True
)

# 섹션: 개요
st.header("개요")
st.write("""
**블리치(BLEACH)**는 일본의 만화가 쿠보 타이토(Tite Kubo)에 의해 창작된 작품으로, 
2001년부터 2016년까지 '주간 소년 점프'에 연재되었습니다. 
이 작품은 고등학생 쿠로사키 이치고가 사신의 힘을 얻으면서 벌어지는 모험과 전투를 다룹니다.
""")

# 섹션: 세계관
st.header("세계관")
st.write("""
블리치의 세계는 크게 세 가지로 나뉩니다:
- **현세**: 인간이 사는 세계
- **소울 소사이어티**: 죽은 영혼들이 모이는 사후 세계
- **웨코문드**: 악령(호로)들이 거주하는 세계

사신들은 이 세상의 균형을 유지하며 악령인 '호로'를 퇴치하고 혼백을 성불시키는 역할을 합니다.
""")

# 섹션: 주요 등장인물 (인터랙티브)
st.header("주요 등장인물")

# 캐릭터 선택 버튼 생성
if st.button("쿠로사키 이치고"):
    st.subheader("쿠로사키 이치고")
    st.image(
        "https://i.pinimg.com/736x/51/aa/f8/51aaf8bdb474c43e135b811a3fe4b239.jpg",
        caption="쿠로사키 이치고",
        use_column_width=True
    )
    st.write("""
    이 작품의 주인공으로, 영혼을 볼 수 있는 능력을 가진 고등학생입니다.
    어느 날 사신 쿠치키 루키아와 만나면서 사신의 힘을 얻고, 
    자신의 마을과 소중한 사람들을 지키기 위해 싸웁니다.
    """)
    st.image(
        "https://i.namu.wiki/i/1Uc3K6ydVGQUUzP-ZCJL302p7BDaX_ebgCwI7OMei3Hf-MoZXnIwWOOyj-f8Exr29ho1xG2HG6DxUEdkcad8Tg.gif",
        caption="이치고의 기술: 월아천충 (Getsuga Tensho)",
        use_column_width=True
    )

if st.button("쿠치키 루키아"):
    st.subheader("쿠치키 루키아")
    st.image(
        "https://i.namu.wiki/i/Wk0HNxKx9y2pDo1k88pUUpCAPHcVga-2ZV0Rud6MKdljfAtBvijixojWdnas1UHgL2btDZiJE76lqDcXHMUZ6g.webp",
        caption="쿠치키 루키아",
        use_column_width=True
    )
    st.write("""
    소울 소사이어티에서 온 사신으로, 이치고에게 자신의 힘을 나눠준 뒤 인간 세계에서 함께 활동합니다.
    그녀는 소울 소사이어티에서 중요한 사건에 휘말리며 이야기가 전개됩니다.
    """)
    st.image(
        "https://i.namu.wiki/i/Pm4Np__yODOoqIoczY7c4udETGvAFE-nsJNItLEMVfFZDduUJoDXRP3V6Dxck2IIG7bguUrfRw5Jn0O3Ozq72w.gif",
        caption="루키아의 기술: 백하벌 (Sode no Shirayuki)",
        use_column_width=True
    )

if st.button("아이젠 소스케"):
    st.subheader("아이젠 소스케")
    st.image(
        "https://i.namu.wiki/i/Tjj_lYI2Y_EAlwOzexBz8DtkRlkCRu6zte9A6yJgCFphiYcSOMhx2wLFjGym7uumXkURQwHVbmCVkW5WAKgD2A.webp",
        caption="아이젠 소스케",
        use_column_width=True
    )
    st.write("""
    소울 소사이어티의 반역자로, 주요 악역 중 하나입니다. 
    그는 강력한 힘과 지능으로 여러 음모를 꾸미며 스토리를 긴장감 있게 이끌어갑니다.
    """)

if st.button("히라코 신지"):
    st.subheader("히라코 신지")
    st.image(
        "https://i.namu.wiki/i/zL9TMcIXmgNaN3VuGfcwx11aLS8oSVqgy3OiITjhgz4BI_Xz8REcsI6QBOpXWlxkWXL3IYZD4K-DC10rmnCPhQ.webp",
        caption="히라코 신지",
        use_column_width=True
    )
    st.write("""
    히라코 신지는 전직 사신이며 바이저드(Vizard)의 리더입니다. 
    그는 독특한 유머 감각과 뛰어난 전투 능력을 가지고 있으며, 
    이치고와 그의 동료들에게 중요한 조언자 역할을 합니다.
    """)

if st.button("쿠치키 뱌쿠야"):
    st.subheader("쿠치키 뱌쿠야")
    st.image(
        "https://i.namu.wiki/i/rmWVQUgSmdQQFpry1-xJyNHUDPMkO-FmgzgJDNMslBB3v5W5zgx9dihhHaOYrIwdw0EvTNWxPY9xmKbDwi1IPA.webp",
        caption="쿠치키 뱌쿠야",
        use_column_width=True
    )
    st.write("""
    뱌쿠야는 6번대 대장으로서 귀족적인 태도와 강력한 전투력을 자랑합니다.

