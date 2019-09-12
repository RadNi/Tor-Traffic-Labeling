TOR Onion Skin Labeling 

How It Works?

The onion_skin_reader.py script tries to read every entry from input file.
    - Inputs:
        - onion_skin file (which our modified TOR client provided for us)
    - Outputs:
        - The file_reader() returns an iterator which in every step provides us a (label, payload) tuple

Example:
    - python3.6 onion_skin_reader.py cells_2_layer_enc
