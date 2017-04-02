# Usage

Find text similarties

<h2>Build corpus for each resource id</h2>
<pre>
./build_corpus.py 1 "Human machine interface for lab abc computer applications","A survey of user opinion of computer system response time","The EPS user interface manag$
</pre>

<h2>Get text similarity for resource id</h2>
<pre>
./get_similarities.py 1 'human'
</pre>

Don't forget to:

<pre>
chmod +x get_similarities.py build_corpus.py
</pre>
