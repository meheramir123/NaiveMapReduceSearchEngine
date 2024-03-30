from mrjob.job import MRJob
import re

class VocabMapper(MRJob):
    def mapper(self, _, line):
        # Skip lines with metadata and empty lines
        if line.startswith('ARTICLE_ID,SECTION_TEXT') or not re.findall(r'\w+', line):
            return

        # Split the line into words
        words = re.findall(r'\w+', line.lower())
        # Emit each word with a count of 1
        for word in words:
            yield word, 1




class VocabReducer(MRJob):
    def reducer(self, word, counts):
        try:
            # Convert counts to integers and sum them up
            total_count = sum(int(count) for count in counts)
            # Emit the word along with its total count
            yield word, total_count
        except ValueError:
            # Handle invalid counts gracefully
            pass

if __name__ == '__main__':
    VocabReducer.run()



if __name__ == '__main__':
    VocabMapper.run()
    VocabReducer.run()

