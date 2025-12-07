# este file indica qué estamos haciendo 
# Descripción de la tarea a realizar
Feature: API simple de JSONPlaceholder

    # Background se ejecuta antes de cualquier escenario 
    # y aplica a cualquiera de ellos 

    Background:
        # Dado el estado del sistema que debe validar
        Given la API está disponible

    # Escenario de lo que se va a probar
    # en este caso obtener un registro desde posts
    Scenario: Obtener posts
        # When representa el cómo se ejecuta el Given anterior
        When hago GET a "/posts"
        # Then representa el resultado esperado 
        Then el status debe ser 200

    # creamos otro Scenario pero ahora con peticiones múltiples
    Scenario Outline: Probar diferentes endpoints
        When hago GET a <endpoint>
        Then el status debe ser <status>

        # enumeramos las peticiones 
        Examples:
            | endpoint    | status |
            | "/posts/1"  | 200    |
            | "/users"    | 200    |
            | "/invalid"  | 404    |

    # creamos otro Scenario que use POST mediante tabla
    Scenario: Crear post con tabla
        # los campos necesarios los obtenemos entrando a la documentación del endpoint
        When hago POST a "/posts" con:
            | title  | Mi titulo |
            | body   | Mi contenido |
            | userId | 1 |
        Then el status debe ser 201