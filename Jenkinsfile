pipeline {
    agent any

    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                echo 'Descargando la receta de BioGuard...'
                checkout scm
            }
        }

        stage('Build (Cocinar)') {
            steps {
                echo 'Cocinando la imagen Docker...'
                sh 'docker build -t bioguard-app .'
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Auditando con PyBuilder dentro del contenedor...'
                // Ejecutamos pyb dentro de la imagen que acabamos de crear
                sh 'docker run --rm bioguard-app pyb' 
            }
        }

        stage('Deploy (Entrega)') {
            steps {
                echo 'Desplegando en Puerto Seguro...'
                sh 'docker rm -f bioguard-prod || true'
                // MODIFICACIÓN: Cambiamos -p 5000:5000 por -p 8443:5000 [cite: 34]
                sh 'docker run -d --name bioguard-prod -p 8443:5000 bioguard-app'
                echo '¡Sistema servido en http://localhost:8443!'
            }
        }
    }

    post {
        always {
            echo 'Limpiando la cocina...'
            sh 'docker image prune -f'
        }
    }
}
