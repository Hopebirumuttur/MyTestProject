import asyncio
from desktop_notifier import DesktopNotifier, Urgency, Button, ReplyField, DEFAULT_SOUND

async def main():
    notifier = DesktopNotifier(app_name="Sample App")

    # 🔵 Event: programı durdurmak için
    stop_event = asyncio.Event()

    # 🔵 Bildirimi oluştur
    await notifier.send(
        title="Julius Caesar",
        message="Sen de mi Bürütüs?",
        urgency=Urgency.Critical,
        buttons=[
            Button(
                title="Mark as read",
                on_pressed=lambda: (
                    print("Marked as read"),
                    stop_event.set()         # programı bitir!
                ),
            )
        ],
        reply_field=ReplyField(
            on_replied=lambda text: print("Brutus cevabı:", text),

        ),
        on_dispatched=lambda: print("Notification showing"),
        on_clicked=lambda: print("Notification clicked"),
        on_dismissed=lambda: (
            print("Notification dismissed"),
            stop_event.set()     # bildirimi kapatınca da bitir
        ),
        sound=DEFAULT_SOUND,
    )

    # 🔵 Bildirime etkileşim gelene kadar bekle
    await stop_event.wait()

    print("Program bitti.")

# 🔵 Programı başlat
asyncio.run(main())
