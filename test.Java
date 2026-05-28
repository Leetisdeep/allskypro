import java.util.ArrayList;
import java.util.List;

public class test {

    public static List<String> splitOntoChunks(String str, int chunkSize) {
        List<String> chunks = new ArrayList<>();
        int length = str.length();
            
        for (int i = 0; i < length; i += chunkSize) {
            int end = Math.min(length, i + chunkSize);
            chunks.add(str.substring(i, end));
        }
        return chunks;
    }

    public static void main(String[] args) {
        System.out.println(splitOntoChunks("123456",3));
    }
}