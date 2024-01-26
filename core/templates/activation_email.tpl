{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account Activation
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
Youre token: <br>

 <a href='http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{token}}'>click to verified</a>
<br>
 <b>Alert:</b>
 <p>dont get youre token code to anyone</P>
{% endblock %}
