# Taken and adapted from https://stackoverflow.com/questions/24398536/named-entity-recognition-with-regular-expression-nltk
# Used under CC-BY-SA
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

def get_continuous_chunks(text):
	'''
	simply returns a list of all named entities in the text provided
	'''
	chunked = ne_chunk(pos_tag(word_tokenize(text)))
	prev = None
	continuous_chunk = []
	current_chunk = []

	for i in chunked:
		if type(i) == Tree:
			current_chunk.append(" ".join([token for token, pos in i.leaves()]))
		elif current_chunk:
			named_entity = " ".join(current_chunk)
			if named_entity not in continuous_chunk:
				continuous_chunk.append(named_entity)
				current_chunk = []
		else:
			continue
	if current_chunk:
		named_entity = " ".join(current_chunk)
		if named_entity not in continuous_chunk:
			continuous_chunk.append(named_entity)
			current_chunk = []
	return continuous_chunk
	
def tag_entity_text(text):
	'''
	returns the text, separated by part of speech, with the named entities 
	tagged and the named entities strung into a single string (eg "Acadmic Provost")
	'''
	chunked = ne_chunk(pos_tag(word_tokenize(text)))
	out = []

	for i in chunked:
		if type(i) == Tree:
			# This method gives you each word of the named entity separately
			#out.append((i.label(), [token for token, pos in i.leaves()]))
			# This method give you the entire entity as one string
			out.append((i.label(), " ".join([token for token, pos in i.leaves()])))
		else:
			out.append(i[0])
	return out

def tag_entity_text_v0(text):
	'''
	returns the text, separated by part of speech, with the named entities 
	tagged and the named entities' words as separate items in a list (eg ["Acadmic", "Provost"])
	'''
	chunked = ne_chunk(pos_tag(word_tokenize(text)))
	#print(chunked)
	prev = None
	continuous_chunk = []
	current_chunk = []
	out = []

	for i in chunked:
		if type(i) == Tree:
			current_chunk.append(" ".join([token for token, pos in i.leaves()]))
			out.append((i.label(), [token for token, pos in i.leaves()]))
		elif current_chunk:
			named_entity = " ".join(current_chunk)
			if named_entity not in continuous_chunk:
				continuous_chunk.append(named_entity)
				current_chunk = []
		else:
			out.append(i[0])
	
	if current_chunk:
		named_entity = " ".join(current_chunk)
		#print(named_entity)
		if named_entity not in continuous_chunk:
			continuous_chunk.append(named_entity)
			current_chunk = []
	return out

with open("../pdf_scrape/test.txt") as f:
	txt = f.read()
	
	
fh = open("test_nlp.txt","w")
for item in tag_entity_text(txt):
	fh.write(str(item) + " ")
	if (item=='.'):
		fh.write("\n")
		
fh.close()