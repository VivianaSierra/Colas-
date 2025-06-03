# Colas-
Descripcion del problema
Centro de Atención Telefónica
Imagina un servicio de soporte técnico o atención al cliente. Cuando un usuario llama, su llamada no siempre es atendida de inmediato si todos los agentes están ocupados. Lo que sucede es que la llamada se pone en una cola.

Encolar (enqueue): Cada vez que un cliente llama y no hay un agente disponible, su llamada se añade al final de una cola de espera. En este momento, al cliente se le puede reproducir un mensaje tipo "Todas nuestras líneas están ocupadas, por favor, espere, su llamada es muy importante para nosotros".

Desencolar (dequeue): Tan pronto como un agente queda libre, el sistema toma la primera llamada que entró en la cola (la que lleva más tiempo esperando) y la conecta con ese agente. La llamada se "desencola".

Frente (front/peek): El supervisor del call center podría querer saber qué llamada es la siguiente en ser atendida, o qué cliente ha estado esperando más tiempo. Esto sería mirar el "frente" de la cola.

Está vacía (isEmpty): Si no hay ninguna llamada esperando, la cola está vacía, y los agentes libres pueden estar esperando nuevas llamadas.

Tamaño (size): El sistema puede mostrar cuántas llamadas están actualmente en espera, lo que ayuda a monitorear la carga de trabajo y el tiempo de espera.
