from telegram import Update
from telegram.ext import CallbackContext

def lugat(update: Update, context: CallbackContext):
	update.message.reply_text("안녕하세요 — Salom — annyeonghaseyo\n감사합니다 — Rahmat — kamsahamnida\n네 — Ha — ne\n아니요 — Yo‘q — aniyo\n사랑 — Sevgi — sarang\n학교 — Maktab — hakgyo\n집 — Uy — jip\n물 — Suv — mul\n밥 — Guruch/taom — bap\n친구 — Do‘st — chingu\n이름 — Ism — ireum\n책 — Kitob — chaek\n선생님 — O‘qituvchi — seonsaengnim\n학생 — Talaba — haksaeng\n어디 — Qayerda? — eodi\n왜 — Nega? — wae\n언제 — Qachon? — eonje\n무엇 — Nima? — mueot\n좋아요 — Yaxshi! — joayo\n몰라요 — Bilmayman — mollayo  ")
