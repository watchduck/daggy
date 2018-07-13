# Daggy

Daggy is a personal wiki software currently in development.
Its page inheritance implements a
[directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG)
rather than a tree structure. So each page can have multiple parents,
allowing real-life friendly page categorization like
_Swedish crime novels_ under _Swedish books_ and under _crime novels_.

The backend uses [Django](https://en.wikipedia.org/wiki/Django_%28web_framework%29),
serving the results as JSON using the [REST framework](http://www.django-rest-framework.org/).

The frontend is a separate [Vue.js](https://en.wikipedia.org/wiki/Vue.js) single-page application.

Posting from the frontend to the backend requires
[CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing),
implemented using
[django-cors-headers](https://github.com/ottoyiu/django-cors-headers).

## Example

There is a functional read-only version of the first commit, created to show a bug in the frontend:<br>
Front: http://daggy1.watchduck.net/nodes &nbsp;
Back: http://back-daggy1.watchduck.net/api/node/