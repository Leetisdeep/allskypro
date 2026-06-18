package pro.sky.telegrambot.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import java.time.LocalDateTime;

@Entity
@Table
public class Notification {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long chatId;

    private String text;

    private LocalDateTime date;

    public Long getId() {
        return id;
    }

    public Notification setId(Long id) {
        this.id = id;
        return this;
    }

    public Long getChatId() {
        return chatId;
    }

    public Notification setChatId(Long chatId) {
        this.chatId = chatId;
        return this;
    }

    public String getText() {
        return text;
    }

    public Notification setText(String text) {
        this.text = text;
        return this;
    }

    public LocalDateTime getDate() {
        return date;
    }

    public Notification setDate(LocalDateTime date) {
        this.date = date;
        return this;
    }
}
