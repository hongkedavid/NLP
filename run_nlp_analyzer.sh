# Parse commit logs, manpage or specification
cat commit.log.all | grep -v "Author: \|Date: \|commit " | python parse_tree_commit.py > commit.full
cat manpage | python parse_tree.py > manpage.filter
cat tcpros.doc | python parse_tree.py > tcpros.doc.out
cat tcpros.manpage | python parse_tree.py > tcpros.manpage.out
cat rfc1035.txt | head -n2736 | tail -n2608 | python parse_tree_rfc.py > rfc1035.filter

# Topic modeling
cat commit.full | python topic_model.py
cat manpage.filter | python topic_model.py
cat tcpros.manpage.out tcpros.doc.out | sed 's/:\./\./g' | python topic_model.py
