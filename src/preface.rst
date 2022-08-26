.. raw:: latex

    \frontmatter
    \let\partBackup\part
    \let\chapterBackup\chapter
    \let\sectionBackup\section
    \let\part\chapter
    \let\chapter\section
    \let\section\subsection

Preface
-------

Welcome to the preface! In time, this preface will contain more information
about the purpose of this book, suggested ways of reading it, etc. For now,
it just contains some basic information on some notation you'll see throughout
the book.

.. _example-code:

Example code
~~~~~~~~~~~~

Some chapters in the book rely on example code that we provide through the
following repository on GiHub:

https://github.com/cs-apps-book/examples

When referring to individual example files, we will use the full path
within that repository. For example, ``getting-started/code-organization/arithmetic.py``

Additional information boxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Throughout the book, you will encounter four types of information boxes:

.. technical-details:: Technical Details

   This kind of box provides deeper technical details about something
   that was just explained. These technical details are not essential to
   understanding the concept or skill that precedes this box, and are
   mostly provided for readers who want to dig a bit deeper (specially
   if you're the kind of learner who has an easier time understanding new
   concepts with those lower-level details).

   This means that you can usually safely skip these boxes on your first
   read through a chapter. However, if you do so, we still recommend
   revisiting these boxes once you become more comfortable with the material.

.. common-pitfalls:: Common Pitfalls

   This kind of box alerts you to common pitfalls that beginners sometimes
   make. Make sure to read this box so you don't fall into those pitfalls yourself!

.. tip:: Debugging Tips

   As we'll describe later in the book, debugging issues in your code can sometimes
   feel like solving a murder mystery where you are both the detective and the murderer.
   Pinpointing the cause of errors in your code is a skill that takes time to
   build, so we've made sure to include debugging tips throughout the book so
   you know what to look out for when your code fails in certain ways.

.. info-note::

   Notes are used to clarify certain concepts, or to call out information that doesn't
   fit into any of the above boxes.


Special sections
~~~~~~~~~~~~~~~~

Sometimes, entire sections of the book will revolve around the kind of technical
details we would include in a Technical Details box (as described above). Look out for sections with the gears icon like this:

.. raw:: html

   <blockquote>
   <div class="section-technical-details section" id="technical-details-section">
   <h2>Technical Details Section</h2>
   </div>
   </blockquote>

When you see a section like this, remember that you can safely skip it
if you want to, but may want to revisit it later on.


.. raw:: latex

    \let\part\partBackup
    \let\chapter\chapterBackup
    \let\section\sectionBackup
    \mainmatter