text = "Hoffmann was appointed by President Ricardo Lagos in March 2000 to serve as Executive Secretary of the National Environment Commission,[4] a precursor of Chile's Ministry for the Environment. During her tenure she oversaw the creation of the national hiking trail network Sendero de Chile, improved the System of Environmental Impact Assessment (SEIA), and worked to implement environmental education programs and improve air quality in Santiago.[12] During her tenure she encountered criticism from business interests for her environmentalist stances and from environmental groups for her perceived lack of influence within the administration.[13] Following the controversial approval of petcoke for gas-fired generators over her objections,[14] Hoffmann resigned in October 2001, stating that she no longer felt she was supported by Lagos or the Ministers.[6] She returned to work with Defensores del Bosque and prepared for her eventual retirement.[4]"
from nltk.tokenize import sent_tokenize
sentences = []
sentences.append(sent_tokenize(text))
sentences = [y for x in sentences for y in x] # flatten list
for i in sentences:
    print("############")
    print(i)