# coding=UTF-8
from __future__ import division
import re
from EmailParser.py import dataextract
  
class SummaryTool(object):
 
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")
 
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")
 
    def sentences_intersection(self, sent1, sent2):
 
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))
 
        if (len(s1) + len(s2)) == 0:
            return 0
 
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)
 
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    def get_sentences_ranks(self, content):
 
        sentences = self.split_content_to_sentences(content)
 
        n = len(sentences)

        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])
 
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic
 
    def get_best_sentence(self, paragraph, sentences_dic):
        sentences = self.split_content_to_sentences(paragraph)
 
        if len(sentences) <= 2:
            return ""
 
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s
 
        return best_sentence
 
    def get_summary(self, title, content, sentences_dic):
 
        paragraphs = self.split_content_to_paragraphs(content)
 
        summary = []
        summary.append(title.strip())
        summary.append("")
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:                    
                summary.append(sentence)
 
        return ("\n").join(summary)
 
 
# Main method, just run "python summary_tool.py"
def main():
 
    title = ""
 
    content = """
    Dear Rapt Studio, 

    My name is Nicole Bella, I'm a student at Cal State Long Beach, and part of the BFA Graphic Design program. I'm reaching out to you because I would love to have an opportunity to be part of your studio as an intern this summer. 

    I've admired your studio's work for quite some time and I would love to gain experience in making such strong and beautiful design. When I look at your work, it feels refreshing, bold, and new. Your studio isn't afraid to take the extra step and time to make the project that much more special. I also admire the connection your studio makes with design and space because it flows so seamlessly; you consider every detail, big and small, to make a wholesome experience. It is apparent that you are so passionate and driven in what you do. I would love to work in such an environment because I would learn so much about making designs that are impactful. 

    I hope you consider looking at my resume and portfolio; I believe I can be a positive addition to your studio. I am a determined and hardworking person, who would love to be inspired and take guidance from professionals like you. 

    I've attached my resume to this email, and a link to my portfolio. If you have any thoughts or questions, please don't hesitate to contact me. 


    Have a wonderful day!


    Nicole Bella


    nikolnicolebella@gmail.com
    619.518.5939
    Portfolio

    """
 
    st = SummaryTool()
    sentences_dic = st.get_sentences_ranks(content)
    summary = st.get_summary(title, content, sentences_dic)
 
    print summary
 
    #print ""
    #print "Original Length %s" % (len(title) + len(content))
    #print "Summary Length %s" % len(summary)
    #print "Summary Ratio: %s" % (100 - (100 * (len(summary) / (len(title) + len(content)))))
 
 
if __name__ == '__main__':
    main()