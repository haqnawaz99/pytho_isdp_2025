========================================
Diagrams for the Strings Chapter
========================================
Copy each code block below into https://mermaid.live and export as PNG or SVG.
Then insert the image into CHAPTER_Strings.docx where suggested.

----------------------------------------
Diagram 1: String as sequence of characters
Place after "What is a String?" (Concept 1).
----------------------------------------

flowchart LR
    subgraph s["String: Lahore"]
        L[L]
        a[a]
        h[h]
        o[o]
        r[r]
        e[e]
    end

----------------------------------------
Diagram 2: Concatenation
Place after "We can join strings using the + operator" (Concept 1).
----------------------------------------

flowchart LR
    A["Assalamu"]
    B[" "]
    C["Alaikum"]
    A --> plus1[+]
    B --> plus1
    plus1 --> plus2[+]
    C --> plus2
    plus2 --> R["Assalamu Alaikum"]

----------------------------------------
Diagram 3: strip, lstrip, rstrip
Place before the "Code:" block in section 3.2 Removing Whitespace.
----------------------------------------

flowchart TB
    subgraph original["Original string"]
        L1[spaces]
        T1[Fajr Prayer]
        R1[spaces]
    end
    subgraph strip["strip() removes both"]
        T2[Fajr Prayer]
    end
    subgraph lstrip["lstrip() removes left only"]
        T3[Fajr Prayer + spaces]
    end
    subgraph rstrip["rstrip() removes right only"]
        T4[spaces + Fajr Prayer]
    end

----------------------------------------
Diagram 4: Method chaining
Place before the "Code:" block in section 3.9 Chaining Methods.
----------------------------------------

flowchart LR
    A["  assalamu alaikum  "]
    B[strip]
    C[assalamu alaikum]
    D[title]
    E[Assalamu Alaikum]
    A --> B --> C --> D --> E

========================================
