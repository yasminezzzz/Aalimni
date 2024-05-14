  document.getElementById('offer-select').addEventListener('change', function() {
            var selectedOffer = this.value;
            var scheduleContainers = document.querySelectorAll('.schedule-container');
            var allScheduleBody = document.getElementById('all-schedules-body');
        
            scheduleContainers.forEach(function(container) {
                if (selectedOffer === '') {
                    container.style.display = ''; // Afficher tous les emplois du temps si aucune offre n'est sélectionnée
                } else {
                    if (container.id === selectedOffer) {
                        container.style.display = ''; // Afficher le tableau de l'offre sélectionnée
                    } else {
                        container.style.display = 'none'; // Masquer les autres emplois du temps
                    }
                }
            });
        
            if (selectedOffer === '') {
                allScheduleBody.style.display = ''; // Afficher le tableau des emplois du temps par défaut si aucune offre n'est sélectionnée
            } else {
                allScheduleBody.style.display = 'none'; // Masquer le tableau des emplois du temps par défaut si une offre est sélectionnée
            }
        });