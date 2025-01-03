<h1>Welcome to the Repetitive Cafe</h1>
<?php
    $drinks = [
        "sprite" => 2.00,
        "water" => 1.00,
        "sweet tea" => 2.50,
        "thai tea" => 3.50
    ];
    $pastries = ["donut", "croissant", "hawaiian bread", "cookie"];
?>
<h3>Drinks!</h3>
<ul>
    <?php for ($i = 0; $i < count($pastries); $i++): ?>
        <li><b><?= ucwords($pastries[$i]) ?></b></li>
    <?php endfor ?>
</ul>
<h3>Pastries! ($2 each)</h3>
<ul>
    <?php foreach ($drinks as $drink => $price): ?>
        <li><b><?= ucwords($drink) ?>:</b> $<?= $price ?></li>
    <?php endforeach; ?>
</ul>