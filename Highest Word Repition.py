# Program to find the highest number of word repetition in the Paragraph
# 1. Find out the words number with constant number of letters
# 2. Find out the highest number of letter in the list
# 3. Find out the highest repetition of certain word with its list upto top 10.
# 4. Find out the most repeteated word in certain sentence and name its position also.



word_pack = "In recent years Pokhara independently has become one of the most popular tourist destinations in the World. Although due to less number of manmade structures it has highly been benefitted by natural sceneries, aesthetic looks and spiritual environment. Several hundred thousands of tourists from all over the world visit Nepal from which most of them have greater intention to visit Pokhara. Also, Pokhara bears higher ratio of tourists return rate. Higher natural variations with greater number of sacred and mysterious places have provided so much importance for this tourist destination.     Frequently visited places of Pokhara includes Phewa lake, Begnas Lake, Sarangkot, Mahendra Cave, Bat Cave, Trekkings on the foot of Himalayas, etc. In addition to it local tourists have higher urge to visit places like: Barahi Temple, Gandaki Rainbow Trout Farm (Bhurjungkhola), Methlang etc.     Along with Sarangkot, Dhikidanda(Harpakh) is also known as the most distinctive paragliding spot throughout the country. But in recent years it has just been limited only to Sarangkot. Flow of tourists seems to have completely stopped in Dhikidanda area nowadays.     Primarily, Dhikidanda can be accessed from the Besichowk located in the midway of Machhapuchhre Gramin Marga which starts from Pokhara, Bagar to Tatopani of Machhapuchhre Rural Municipality. Through vehicle Dhikidanda can be reached in maximum time of 30 minutes covering a portion of Gharmi and Kurechaur Village. Altenatively, from Batulechaur by covering majority of Gharmi and Kurechaur village. Although both the routes intersect and intersect and move though the same route from Gharmi, Maidan onwards, Besichowk route is preferred more as it offers less span of earthen road. Nearest tourist destination is Gandaki Rainbow Trout Farm which is accessible from same Besichowk spot through Churunga Village. Gandaki Rainbow Trout Farm ranks higher in the most visited places in Pokhara throughout the year but lacks proper accommodation and recreational facility. As, we know tourists have higher preference to stay in rural places having  proper view of adjoining areas with complete Himalayas scenery which is properly supplied with services of recreation, refreshment, spiritually sound and aesthetically perfect.  As a multinational Company, Ncell has established various structures throughout the country and made distinctive contribution for the tourism sector. Due to the fact that Ncell supports for the positive social changes, I want to forward proposal for the establishment of “Ncell Park – Dhikidanda”. After successful implementation of this Project it seems like revealing the hidden mystery having potentiality of unlimited economic activity.  Through preliminary research, the basic components Ncell Park – Dhikidanda includes should be: 1.	Trekking Facility  2.	Bunjee Jump  3.	High Swing  4.	Swimming Pool 5.	Zip Line  6.	Day time Fooding facility 7.	Hotel with 100 people accommodation capacity (Should be planned to extend for 200) 8.	Billiard Board/Ncell Logo visible from Pokhara Valley  9.	Land should be acquired so as to have large Seminar Hall in Future.     "


word_list = []
w_n_dict = {}
w_rep_dict = {}
word_counter = 0
total_characters = len(word_pack)
start = 0
word = ""

# Word List
for counter in range(total_characters):
    if (word_pack[counter] != " " and (((word_pack[counter] == "," or word_pack[counter] == ".") or (word_pack[counter] == '"' or word_pack[
        counter] == "'")) or ((word_pack[counter] == "_" or word_pack[counter] == ";") or (word_pack[counter] == ":" or
            word_pack[counter] == "?")))==False):
        word = word + word_pack[counter]

    elif (((word_pack[counter] == "," or word_pack[counter] == ".") or (word_pack[counter] == '"' or word_pack[
        counter] == "'")) or ((word_pack[counter] == "_" or word_pack[counter] == ";") or (word_pack[counter] == ":" or
            word_pack[counter] == "?"))):
        word_list.append(word)
        word = ""

        word = word + word_pack[counter]
        word_list.append(word)
        word = ""

    else:
        if word != "":
            word_list.append(word)
            word = ""
        else:
            pass
# End--------------------

# Letter and Frequency Dictionary
for item in word_list:
    w_n_dict[item] = len(item)
# End--------------------
# Letter number and frequency dict
l_n_dict = {}
for item in word_list:
    w_length = len(item)
    w_n_dict[item] = w_length
    try:
        l_n = l_n_dict[w_length]
        l_n_dict[w_length] = l_n+1
    except:
        l_n_dict[w_length] = 1
l_n_value = []
l_n_key = []
# End--------------------
# Letter number and frequency dict Splitter in list
for key,value in l_n_dict.items():
    l_n_key.append(key)
    l_n_value.append(value)
l_n_value.sort(reverse=True)
# End--------------------
l_n_dict_sorted = {}
for i in sorted(l_n_dict, key=l_n_dict.get, reverse=True):
    l_n_dict_sorted[i] = l_n_dict[i]
print(l_n_dict_sorted)
# Numbers Frequency Analyzing Completed

print(word_list)
for item in word_list:
    r_count = 0

    for item1 in word_list:
        if item == item1:
            r_count +=1
    w_rep_dict[item] = r_count
w_rep_dict_sorted = {}

for i in sorted(w_rep_dict, key=w_rep_dict.get, reverse=True):
    w_rep_dict_sorted[i] = w_rep_dict[i]
print(w_rep_dict_sorted)




max = len(word_list)
word_list1 = []
word_list2 = []
print(w_rep_dict_sorted['.'])
for j in range(len(word_list)):
    if word_list[j] != ".":
        word_list1.append(word_list[j])
    else:
        word_list2.append(word_list1)
        word_list1 = []

print(word_list1)
print(word_list2)

print (w_rep_dict_sorted, "hello")





