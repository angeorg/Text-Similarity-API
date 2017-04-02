# Usage

Find text similarties

<h2>Build corpus for each resource id</h2>
<pre>
./build_corpus.py 1 "Human machine interface for lab abc computer applications","A survey of user opinion of computer system response time","The EPS user interface management system","System and human system engineering testing of EPS","Relation of user perceived response time to error measurement","The generation of random binary unordered trees","The intersection graph of paths in trees","Graph minors IV Widths of trees and well quasi ordering","Graph minors A survey"
</pre>

<h2>Get text similarity for resource id</h2>
<pre>
./get_similarities.py 1 'human'
</pre>

Don't forget to:

<pre>
chmod +x get_similarities.py build_corpus.py
</pre>
