package pro.sky.telegrambot.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import pro.sky.telegrambot.jpa.NotificationRepository;
import pro.sky.telegrambot.model.Notification;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Service
@RequiredArgsConstructor
public class NotificationService {

    private NotificationRepository notificationRepository;
    private static final Pattern PATTERN = Pattern.compile("(\\d{2}\\.\\d{2}\\.\\d{4}\\s\\d{2}:\\d{2})(\\s+)(.+)");

    public void saveNotification(Long chatId, String msg) {
        Matcher matcher = PATTERN.matcher(msg);
        if (matcher.matches()) {
            String date = matcher.group(1);
            String text = matcher.group(3);
            Notification notification = new Notification()
                    .setChatId(chatId)
                    .setText(text)
                    .setDate(LocalDateTime.parse(date, DateTimeFormatter.ofPattern("dd.MM.yyyy HH.mm")));
            notificationRepository.save(notification);
        }
    }

    public List<Notification> getNotifications() {
        return notificationRepository.findAll();
    }

    public void deleteAll(List<Notification> notifications) {
        notificationRepository.deleteAll(notifications);
    }
}
