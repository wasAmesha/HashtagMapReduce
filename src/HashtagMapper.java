import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class HashtagMapper extends Mapper<Object, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text hashtag = new Text();

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString().toLowerCase(); // assuming Text_Lower field
        StringTokenizer tokenizer = new StringTokenizer(line, " ,.!?:;\"'()[]{}<>|");

        while (tokenizer.hasMoreTokens()) {
            String word = tokenizer.nextToken();
            if (word.startsWith("#") && word.length() > 1) {
                hashtag.set(word);
                context.write(hashtag, one);
            }
        }
    }
}
