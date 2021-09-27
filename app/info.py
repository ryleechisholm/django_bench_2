from dataclasses import dataclass
from typing import List

@dataclass
class Subject:
    key_title: str
    title: str
    info: str
    specs: List[str]


SUBJECTS = [ Subject("artists", "Artists", "I have drawn a lot of inspiration from many artists, both new and old.  I especially enjoy the exploration of darker fears and feelings.", ["Van Goph", "Picasso", "@slimyswampghost"]), Subject("musicians","Musicians", "Music is a background enjoyment of mine.  I do not make music but I love it as a form of expression.", ["Imagine Dragons", "Fall Out Boy", "Young The Giant"]), Subject("writers", "Writers", "Reading is one of my favorite hobbies and can really get me thinking on morality and human nature.  I am a bit of a philosophy nerd.", ["James Dashner", "Suzanne Collins", "Neal Shusterman", "Malcolm Gladwell"])]
