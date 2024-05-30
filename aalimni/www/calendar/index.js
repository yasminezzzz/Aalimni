document.addEventListener('DOMContentLoaded', function() {
    var offerOptions = document.querySelectorAll('.offer-option');

    offerOptions.forEach(function(option) {
        option.addEventListener('click', function() {
            // Remove 'active' class from all options
            offerOptions.forEach(function(opt) {
                opt.classList.remove('active');
            });
            
            // Add 'active' class to the clicked option
            this.classList.add('active');
            
            var selectedOffer = this.textContent;
            var scheduleContainers = document.querySelectorAll('.schedule-container');
            var allSchedulesContainer = document.getElementById('all-schedules');

            scheduleContainers.forEach(function(container) {
                if (selectedOffer === 'All offers') {
                    container.style.display = 'block'; // Afficher tous les emplois du temps
                } else {
                    if (container.id === selectedOffer) {
                        container.style.display = 'block'; // Afficher l'emploi du temps de l'offre sélectionnée
                    } else {
                        container.style.display = 'none'; // Masquer les autres emplois du temps
                    }
                }
            });

            if (selectedOffer === 'All offers') {
                allSchedulesContainer.style.display = 'block'; // Afficher le tableau de tous les emplois du temps par défaut
            } else {
                allSchedulesContainer.style.display = 'none'; // Masquer le tableau de tous les emplois du temps par défaut
            }
        });
    });

// Fonction pour détecter les conflits d'offres et ajuster la hauteur des créneaux horaires
function adjustSlotHeights() {
    var scheduleRows = document.querySelectorAll('.schedule-body tr');

    scheduleRows.forEach(function(row) {
        var slots = row.querySelectorAll('td');

        // Créer un dictionnaire pour stocker les offres pour chaque créneau horaire
        var offersBySlot = {};

        // Parcourir chaque slot et regrouper les offres par créneau horaire
        slots.forEach(function(slot) {
            var offer = slot.querySelector('span');
            if (offer) {
                var offerTime = offer.dataset.startTime; // Récupérer l'heure de début de l'offre
                if (!offersBySlot[offerTime]) {
                    offersBySlot[offerTime] = [];
                }
                offersBySlot[offerTime].push(slot);
            }
        });

        // Ajuster dynamiquement la hauteur des slots en cas de conflits
        for (var slotTime in offersBySlot) {
            var slotOffers = offersBySlot[slotTime];
            if (slotOffers.length > 1) {
                var newHeight = 100 / slotOffers.length + '%'; // Calculer la nouvelle hauteur
                slotOffers.forEach(function(slot, index) {
                    // Dupliquer le slot en ajustant la hauteur
                    var clonedSlot = slot.cloneNode(true);
                    clonedSlot.style.height = newHeight;
                    row.insertBefore(clonedSlot, slot.nextSibling);
                });
            }
        }
    });
}

});
