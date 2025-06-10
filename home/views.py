from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    summary_lines = []
    summary_lines.append("--- Übersicht des HTTP-Requests ---")
    summary_lines.append(f"Methode: {request.method}")
    summary_lines.append(f"Pfad: {request.path}")
    summary_lines.append(f"Ist gesichert (HTTPS): {request.is_secure()}")
    summary_lines.append(f"Ist AJAX (XHR): {request.headers.get('x-requested-with') == 'XMLHttpRequest'}")
    
    summary_lines.append("\nGET-Parameter (Query String):")
    if request.GET:
        for key, value in request.GET.items():
            summary_lines.append(f"  {key}: {value}")
    else:
        summary_lines.append("  Keine GET-Parameter.")

    summary_lines.append("\nPOST-Parameter (Formulardaten):")
    if request.method == 'POST':
        if request.POST:
            for key, value in request.POST.items():
                summary_lines.append(f"  {key}: {value}")
        else:
            summary_lines.append("  Keine POST-Parameter (Body könnte leer sein oder JSON/Dateien enthalten).")
        # Hinweis: request.body enthält den Rohinhalt, z.B. für JSON
        if request.body and request.headers.get('content-type') == 'application/json':
             summary_lines.append(f"  Raw JSON Body: {request.body.decode('utf-8')}")
    else:
        summary_lines.append("  POST-Parameter nur bei POST-Anfragen relevant.")
            
    summary_lines.append("\nAusgewählte HTTP-Header (request.META):")
    # Eine Auswahl relevanter Header
    relevant_headers = [
        'HTTP_HOST', 'HTTP_USER_AGENT', 'REMOTE_ADDR', 'CONTENT_TYPE',
        'CONTENT_LENGTH', 'HTTP_ACCEPT', 'HTTP_REFERER', 'HTTP_COOKIE'
    ]
    for key, value in request.META.items():
        if key in relevant_headers or key.startswith('HTTP_') and not key.startswith('HTTP_X_'): # Alle HTTP_ Header, aber nicht X_
            summary_lines.append(f"  {key}: {value}")
    if not any(key.startswith('HTTP_') for key in request.META):
        summary_lines.append("  Keine oder wenige HTTP-Header im META-Dictionary gefunden.")
        
    summary_lines.append("\nAngemeldeter Benutzer (request.user):")
    if hasattr(request, 'user') and request.user.is_authenticated:
        summary_lines.append(f"  Benutzername: {request.user.username}")
        summary_lines.append(f"  E-Mail: {request.user.email}")
        summary_lines.append(f"  Ist Superuser: {request.user.is_superuser}")
    else:
        summary_lines.append("  Kein Benutzer angemeldet oder 'request.user' nicht verfügbar.")

    summary_lines.append("\n--- Ende der Übersicht ---")
    
    summary_lines.append(f"Session {request.session.items()}")

    
    return render(request, 'home/index.html', {'lines': summary_lines})
    #return HttpResponse("\n".join(summary_lines), content_type='text/plain')