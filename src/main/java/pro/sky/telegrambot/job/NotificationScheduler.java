package pro.sky.telegrambot.job;

import com.pengrad.telegrambot.TelegramBot;
import com.pengrad.telegrambot.request.SendMessage;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import pro.sky.telegrambot.model.Notification;
import pro.sky.telegrambot.service.NotificationService;

import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class NotificationScheduler {

    private final TelegramBot bot;
    private final NotificationService service;

    public NotificationScheduler(TelegramBot bot, NotificationService service) {
        this.bot = bot;
        this.service = service;
    }

    @Scheduled(fixedRate = 60000)
    public void sendNotification() {
        List<Notification> notifications = service.getNotifications().stream()
                .filter(it -> LocalDateTime.now().truncatedTo(ChronoUnit.MINUTES).equals(it.getDate()))
                .collect(Collectors.toList());

        notifications.forEach(notification -> {
            bot.execute(new SendMessage(
                    notification.getChatId(),
                    notification.getText())
            );
        });

        service.deleteAll(notifications);
    }
}
