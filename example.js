Affected Products
Ecosystem
npm (Node Package Manager)

Package Name
example.js

Affected Versions
1.50
Questa versione contiene vulnerabilità critiche che permettono l'esecuzione di codice arbitrario, sfruttando una pipeline nel file index.js per esfiltrare dati sensibili come chiavi SSH.

Patched Versions
1.5.0
La vulnerabilità è stata risolta nella versione 1.5.0, che include controlli aggiuntivi per impedire l'esecuzione di codice non autorizzato e l'accesso a directory sensibili.

Severity
Critical
La vulnerabilità consente agli attaccanti di compromettere completamente il sistema, con un impatto significativo sulla confidenzialità, integrità e disponibilità dei dati.

Vector String
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
Questo rappresenta un attacco remoto con basso livello di complessità, senza necessità di privilegi o interazione dell'utente, con impatti elevati sulla sicurezza.

Weaknesses
CWE-94: Improper Control of Generation of Code ('Code Injection')
Questa debolezza permette agli attaccanti di iniettare codice malevolo che viene eseguito nel contesto dell'applicazione.

Credits
Vulnerabilità scoperta da: @TeknologyGroup
Grazie al contributo del team per aver identificato e segnalato il problema.
