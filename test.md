```mermaid
flowchart TD
     
    A[Search] --> B[Album-Artist]
    B --> newLines["`Album 1
    Album 2
    Album 3
    Album 4
    Album 5`"]

    newLines --> D@{ shape: diamond, label: "Choose One" }
    D --> results["`
    Track 1
        Drums:
        Bass:
        Guitar:
        Vocals:
    Track 2
        Drums:
        Bass:
        Guitar:
        Vocals:
    Etc. 
    `"]     

```
