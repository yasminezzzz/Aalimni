document.getElementById('offer-select').addEventListener('change', function() {
    var selectedOffer = this.value;
    var scheduleContainers = document.querySelectorAll('.schedule-container');
    var allScheduleBodies = document.querySelectorAll('.schedule-body');

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

    allScheduleBodies.forEach(function(scheduleBody) {
        if (scheduleBody.id === `${selectedOffer}-schedule-body`) {
            scheduleBody.style.display = ''; // Afficher le tableau de l'offre sélectionnée
        } else {
            scheduleBody.style.display = 'none'; // Masquer les autres tableaux
        }
    });
});
