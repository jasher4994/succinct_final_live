
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import textstat
test = """
There was, many years ago, a gentleman who had a charming lady for his
wife. They had one daughter only, who was very dutiful to her parents.
But while she was still very young, her mamma died, to the grief of her
husband and daughter. After a time, the little girl's papa married another
lady. Now this lady was proud and haughty, and had two grown-up daughters
as disagreeable as herself; so the poor girl found everything at home
changed for the worse.

But she bore all her troubles with patience, not even complaining to her
father, and, in spite of her hard toil, she grew more lovely in face and
figure every year.

Now the King's son gave a grand ball, and all persons of quality were
invited to it. Our two young ladies were not overlooked. Nothing was now
talked of but the rich dresses they were to wear.

At last the happy day arrived. The two proud sisters set off in high
spirits. Cinderella followed them with her eyes until the coach was out
of sight. She then began to cry bitterly. While she was sobbing, her
godmother, who was a Fairy, appeared before her.

[Illustration]

"Cinderella," said the Fairy, "I am your godmother, and for the sake of
your dear mamma I am come to cheer you up, so dry your tears; you shall go
to the grand ball to-night, but you must do just as I bid you. Go into the
garden and bring me a pumpkin." Cinderella brought the finest that was
there. Her godmother scooped it out very quickly, and then struck it with
her wand, upon which it was changed into a beautiful coach. Afterwards,
the old lady peeped into the mouse-trap, where she found six mice. She
tapped them lightly with her wand, and each mouse became a fine horse. The
rat-trap contained two large rats; one of these she turned into a
coachman, and the other into a postilion. The old lady then told
Cinderella to go into the garden and seek for half-a-dozen lizards.
These she changed into six footmen, dressed in the gayest livery.

When all these things had been done, the kind godmother touching her with
her wand, changed her worn-out clothes into a beautiful ball-dress
embroidered with pearls and silver. She then gave her a pair of glass
slippers, that is, they were woven of the most delicate spun-glass, fine
as the web of a spider.

When Cinderella was thus attired, her godmother made her get into her
splendid coach, giving her a caution to leave the ball before the clock
struck twelve.

[Illustration]

[Illustration]

On her arrival, her beauty struck everybody with wonder. The gallant
Prince gave her a courteous welcome, and led her into the ball-room;
and the King and Queen were as much enchanted with her, as the Prince
conducted her to the supper-table, and was too much occupied in waiting
upon her to partake of anything himself. While seated, Cinderella heard
the clock strike three-quarters past eleven. She rose to leave, the Prince
pressing her to accept an invitation for the ball on the following
evening.

On reaching home, her godmother praised her for being so punctual, and
agreed to let her go to the next night's ball.

Although she seemed to be tired, her sisters, instead of showing pity,
teased her with glowing accounts of the splendid scene they had just left,
and spoke particularly of the beautiful Princess. Cinderella was delighted
to hear all this, and asked them the name of the Princess, but they
replied, nobody knew her. So much did they say in praise of the lady, that
Cinderella expressed a desire to go to the next ball to see the Princess;
but this only served to bring out their dislike of poor Cinderella still
more, and they would not lend her the meanest of their dresses.

The next evening the two sisters went to the ball, and Cinderella also,
who was still more splendidly dressed than before. Her enjoyment was even
greater than at the first ball, and she was so occupied with the Prince's
tender sayings that she was not so quick in marking the progress of time.

[Illustration]

To her alarm she heard the clock strike twelve. She fled from the
ball-room; but in a moment the coach changed again to a pumpkin, the
horses to mice, the coachman and postilion to rats, the footmen to
lizards, and Cinderella's beautiful dress to her old shabby clothes. In
her haste she dropped one of her glass slippers, and reached home, out of
breath, with none of her godmother's fairy gifts but one glass slipper.

When her sisters arrived after the ball, they spoke in terms of rapture of
the unknown Princess, and told Cinderella about the little glass slipper
she had dropped, and how the Prince picked it up. It was evident to all
the Court that the Prince was determined if possible, to find out the
owner of the slipper; and a few days afterwards a royal herald proclaimed
that the King's son would marry her whose foot the glass slipper should be
found exactly to fit.

This proclamation caused a great sensation. Ladies of all ranks were
permitted to make a trial of the slipper; but it was of no use. Cinderella
now said, "Let me try--perhaps it may fit me." It slipped on in a moment.
Great was the vexation of the two sisters at this; but what was their
astonishment when Cinderella took the fellow slipper out of her pocket!

At that moment the godmother appeared, and touched Cinderella's clothes
with her wand. Her sisters then saw that she was the beautiful lady they
had met at the ball, and, throwing themselves at her feet, craved her
forgiveness.

A short time after, she was married to the Prince, to the intense
gratification of the whole Court.

[Illustration]


                 *       *       *       *       *


                            ROUTLEDGE'S
                       THREEPENNY TOY-BOOKS,
                  WITH SIX COLOURED ILLUSTRATIONS,

                     PRINTED BY KRONHEIM & CO.

   5. MY FIRST ALPHABET
   6. MOTHER GOOSE
   7. THE BABES IN THE WOOD
   8. THIS LITTLE PIG
   9. THE OLD WOMAN WHO LIVED IN A SHOE
  10. LITTLE BO-PEEP
  11. NURSERY RHYMES
  12. FARM-YARD ALPHABET
  13. JACK AND THE BEANSTALK
  14. JOHN GILPIN
  15. OLD MOTHER HUBBARD
  16. THE THREE BEARS
  17. THE HOUSE THAT JACK BUILT
  18. THE DOGS' DINNER PARTY
  19. MY MOTHER
  20. THE CATS' TEA PARTY
  21. MORE NURSERY RHYMES
  22. ROBIN REDBREAST
  23. A, APPLE PIE
  24. THE RAILWAY ALPHABET
  25. NURSERY SONGS
  26. NURSERY DITTIES
  27. PUNCH AND JUDY
  28. OUR PETS
  29. CINDERELLA
  30. PUSS-IN-BOOTS
  31. LITTLE RED RIDING-HOOD
  32. WILD ANIMALS
  33. TAME ANIMALS
  34. BIRDS
  35. JACK THE GIANT KILLER
  36. BLUE BEARD
  37. ALADDIN
  38. THE FORTY THIEVES
  39. TOM THUMB
  40. SLEEPING BEAUTY IN THE WOOD

                    GEORGE ROUTLEDGE AND SONS,
                       LONDON AND NEW YORK.





End of the Project Gutenberg EBook of Cinderella, by Anonymous

*** END OF THIS PROJECT GUTENBERG EBOOK CINDERELLA ***

***** This file should be named 23303.txt or 23303.zip *****
This and all associated files of various formats will be found in:
        http://www.gutenberg.org/2/3/3/0/23303/

Produced by David Edwards, Anne Storer and the Online
Distributed Proofreading Team at http://www.pgdp.net (This
file was produced from images generously made available
by The Internet Archive)
"""

def sentence_split(file_name):
    #file = open(file_name, "r")
    #filedata = file_name.read()
    filedata = file_name.split(".")
    sentences = []

    for sentence in filedata:
        sentence = sentence.replace("[^a-zA-Z]", " ")
        sentence = sentence.replace('\n', " ")
        sentence = sentence.replace("  "," ")
        sentence = sentence.replace("[^A-Za-z0-9]+"," ")
        sentence = sentence.replace('"'," ") 
        #only removing single quotes otherwise will lost apostrophes. 
        #These should be removed in tokenization anyway. 
        sentence = sentence.replace(','," ")
        sentence = sentence.strip()


        sentences.append(sentence)
 
    return sentences


def readability(sentences):
    
    readability_scores = []
    for sentence in sentences:
        readability_scores.append(textstat.flesch_reading_ease(sentence))
        
    return readability_scores


print(readability(sentence_split(test)))