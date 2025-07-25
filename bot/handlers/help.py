from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "ℹ️ Көмек")
async def help_command(message: Message):
    help_text = (
        "<b>KAZNET боты бойынша көмек</b>\n\n"
        "📝 <b>Жаңа хабарландыру</b> - Жаңа хабарландыру беру процесін бастау.\n\n"
        "📂 <b>Менің хабарландыруларым</b> - Өзіңіз жариялаған барлық хабарландыруларды көру.\n\n"
        "🏙️ <b>Қаланы өзгерту</b> - Хабарландыру беретін немесе іздейтін негізгі қаланы ауыстыру.\n\n"
        "Ботта мәселе туындаса немесе ұсынысыңыз болса, әкімшілікке хабарласыңыз."
    )
    await message.answer(help_text)