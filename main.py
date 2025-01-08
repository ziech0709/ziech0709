import streamlit as st

# HTML을 사용해 배경 이미지 스타일 적용
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://www.crunchyroll.com/news/latest/2024/9/16/bleach-anime-unleashes-20th-anniversary-video-and-art");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

# Streamlit 앱에 스타일 적용
st.markdown(page_bg_img, unsafe_allow_html=True)

# 웹사이트 제목
st.title("블리치 (BLEACH) - 만화 소개")

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

# 섹션: 주요 등장인물
st.header("주요 등장인물")
st.subheader("쿠로사키 이치고")
st.write("""
이 작품의 주인공으로, 영혼을 볼 수 있는 능력을 가진 고등학생입니다.
어느 날 사신 쿠치키 루키아와 만나면서 사신의 힘을 얻고, 
자신의 마을과 소중한 사람들을 지키기 위해 싸웁니다.
""")

st.subheader("쿠치키 루키아")
st.write("""
소울 소사이어티에서 온 사신으로, 이치고에게 자신의 힘을 나눠준 뒤 인간 세계에서 함께 활동합니다.
그녀는 소울 소사이어티에서 중요한 사건에 휘말리며 이야기가 전개됩니다.
""")

st.subheader("아이젠 소스케")
st.write("""
소울 소사이어티의 반역자로, 주요 악역 중 하나입니다. 
그는 강력한 힘과 지능으로 여러 음모를 꾸미며 스토리를 긴장감 있게 이끌어갑니다.
""")

# 섹션: 주요 스토리 아크
st.header("주요 스토리 아크")
st.write("""
1. **사신 대행 편**: 쿠로사키 이치고가 사신의 힘을 얻고 호로와 싸우기 시작합니다.
2. **소울 소사이어티 편**: 루키아를 구하기 위해 소울 소사이어티에 침입하는 이야기가 전개됩니다.
3. **아란칼 편**: 새로운 적 아란칼과의 전투와 웨코문드에서의 모험이 중심입니다.
4. **천년혈전 편**: 최종 전투로, 퀸시 제왕과의 대규모 전쟁이 펼쳐집니다.
""")

# 섹션: 흥미로운 사실
st.header("흥미로운 사실")
st.write("""
- 블리치는 총 74권으로 완결되었으며, 애니메이션과 영화로도 제작되었습니다.
- 제50회 쇼가쿠칸 만화상 소년 부문을 수상했습니다.
- 타이틀 'BLEACH'는 검은색과 대비되는 흰색(표백)을 강조하기 위해 붙여졌습니다.
""")

# 섹션: 사용자 피드백
feedback = st.text_input("블리치에 대한 의견이나 감상을 남겨주세요!")
if feedback:
    st.write(f"감사합니다! 남겨주신 의견: {feedback}")
