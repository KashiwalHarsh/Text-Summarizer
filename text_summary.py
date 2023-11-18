import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# text = """
# The Avengers, a legendary team of superheroes, have become an iconic symbol in the world of comic books and movies. Created by writer Stan Lee and artist Jack Kirby, the Avengers made their first appearance in 1963, published by Marvel Comics. The team comprises a diverse group of extraordinary individuals, each with their unique abilities and powers, who join forces to protect the world from powerful threats and villains.
# At the core of the Avengers is a sense of unity and collaboration. The team includes iconic characters such as Iron Man (Tony Stark), a brilliant inventor equipped with a high-tech suit of armor; Captain America (Steve Rogers), a super-soldier with enhanced strength and agility; Thor, the Norse god of thunder wielding his enchanted hammer, Mjolnir; Hulk (Bruce Banner), a scientist transformed into a colossal green behemoth when angered; Black Widow (Natasha Romanoff), a skilled spy and master martial artist; and Hawkeye (Clint Barton), an expert marksman with exceptional archery skills.
# Throughout their comic book history and the Marvel Cinematic Universe (MCU) films, the Avengers have faced formidable adversaries, including the powerful alien warlord Thanos, the mischievous Loki, and the sentient robot Ultron. Their adventures have taken them from Earth to other realms and galaxies, showcasing their bravery, teamwork, and unwavering dedication to defending humanity.
# One of the defining features of the Avengers is their ability to overcome their differences and work together as a cohesive unit. Despite their individual strengths and weaknesses, they complement each other, forming a team greater than the sum of its parts. This theme of unity and cooperation has resonated with fans around the world, making the Avengers one of the most beloved and enduring superhero teams in popular culture.
# The success of the Avengers extends beyond the pages of comic books. The MCU, a film franchise produced by Marvel Studios, has brought these characters to life on the big screen, creating a shared cinematic universe that has captivated audiences globally. The Avengers movies, including "The Avengers" (2012), "Avengers: Age of Ultron" (2015), "Avengers: Infinity War" (2018), and "Avengers: Endgame" (2019), have become blockbuster hits, breaking records and leaving a lasting impact on the entertainment industry.
# In conclusion, the Avengers represent the epitome of heroism, showcasing the power of teamwork, diversity, and determination. Their adventures continue to inspire generations, reminding us that when individuals come together for a common purpose, they can overcome any challenge and make a difference in the world.
# """



def summarizer(rawDoc):
    stopwords = list(STOP_WORDS)


    nlp =spacy.load("en_core_web_sm")
    doc=nlp(rawDoc)

    tokens =[token.text for token in doc]

    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1

            else:
                word_freq[word.text] +=1


    max_freq =max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_freq


    sent_tokens =[sent for sent in doc.sents]

    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] =word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]


    select_len =int(len(sent_tokens)*0.3)

    summary =nlargest(select_len,sent_scores,key=sent_scores.get)

    final_summery =[word.text for word in summary]
    summary =' '.join(final_summery)

    return summary,doc,len(rawDoc.split(' ')),len(summary.split(' '))


