  {% if user.is_staff %}
   <hr>
   <ul class="sidebar-nav">
   <li>Staff</li>
   {% if perms.catalog.can_mark_returned %}
   <li><a href="{% url 'all-borrowed' %}">All borrowed</a></li>
   {% endif %}
   </ul>
    {% endif %}
 
