<?php
namespace ifuwml\modules;

use std, gui, framework, ifuwml;
use php\gui\UXDialog; 


class AppModule extends AbstractModule
{

    /**
     * @event hotkey.action 
     */
    function doHotkeyAction(ScriptEvent $e = null)
    {    
$e = $event ?: $e; // legacy code from 16 rc-2

		UXDialog::show('Ddsd', 'WARNING');

        
    }

}
